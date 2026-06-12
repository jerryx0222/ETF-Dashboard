import React, { useState, useEffect, useCallback } from 'react';
import {
  Modal, Table, Input, Button, Space, Alert,
  Typography, Tooltip, Badge
} from 'antd';
import { SearchOutlined, ImportOutlined, ReloadOutlined } from '@ant-design/icons';
import api from '../api/axios';

const { Text } = Typography;

export default function ImportModal({ open, onClose, onImported }) {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);
  const [importing, setImporting] = useState(false);
  const [search, setSearch] = useState('');
  const [selectedKeys, setSelectedKeys] = useState([]);
  const [error, setError] = useState('');
  const [result, setResult] = useState(null);

  const fetchList = useCallback(async () => {
    setLoading(true);
    setError('');
    setResult(null);
    try {
      const res = await api.get('/twse/list/');
      setData(res.data);
    } catch (err) {
      setError(err.response?.data?.error || '無法取得 TWSE ETF 清單，請稍後再試');
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    if (open) {
      setSelectedKeys([]);
      setSearch('');
      setResult(null);
      fetchList();
    }
  }, [open, fetchList]);

  const filtered = data.filter(item =>
    !item.already_imported && (
      !search ||
      item.securities_code.includes(search) ||
      item.securities_abbreviation.includes(search) ||
      (item.issuer || '').includes(search)
    )
  );

  const handleImport = async () => {
    if (!selectedKeys.length) return;
    setImporting(true);
    setError('');
    try {
      const payload = data.filter(d => selectedKeys.includes(d.securities_code));
      const res = await api.post('/twse/import/', payload);
      setResult(res.data);
      setSelectedKeys([]);
      fetchList();
      onImported?.();
    } catch (err) {
      setError(err.response?.data?.error || '匯入失敗');
    } finally {
      setImporting(false);
    }
  };

  const columns = [
    {
      title: '代號',
      dataIndex: 'securities_code',
      width: 80,
      render: (v) => <Text strong>{v}</Text>,
    },
    {
      title: '簡稱',
      dataIndex: 'securities_abbreviation',
      width: 160,
      ellipsis: true,
    },
    {
      title: '發行人',
      dataIndex: 'issuer',
      width: 120,
      ellipsis: true,
    },
    {
      title: '標的指數',
      dataIndex: 'target_index',
      ellipsis: true,
      render: (v) => <Tooltip title={v}><span>{v || '—'}</span></Tooltip>,
    },
    {
      title: '配息',
      dataIndex: 'dividend_frequency',
      width: 70,
      render: (v) => {
        const map = { monthly: '月', quarterly: '季', semi_annual: '半年', annual: '年' };
        return map[v] || '—';
      },
    },
  ];

  return (
    <Modal
      title={
        <Space>
          從 TWSE 匯入 ETF
          <Badge count={data.length} color="blue" overflowCount={999} />
        </Space>
      }
      open={open}
      onCancel={onClose}
      width={900}
      footer={
        <Space style={{ width: '100%', justifyContent: 'space-between' }}>
          <Text type="secondary">
            已選 {selectedKeys.length} 筆，共 {filtered.length} 筆未匯入
          </Text>
          <Space>
            <Button icon={<ReloadOutlined />} onClick={fetchList} loading={loading}>
              重新整理
            </Button>
            <Button onClick={onClose}>關閉</Button>
            <Button
              type="primary"
              icon={<ImportOutlined />}
              disabled={!selectedKeys.length}
              loading={importing}
              onClick={handleImport}
            >
              匯入所選 ({selectedKeys.length})
            </Button>
          </Space>
        </Space>
      }
    >
      {error && (
        <Alert type="error" message={error} showIcon closable
          onClose={() => setError('')} style={{ marginBottom: 12 }} />
      )}
      {result && (
        <Alert
          type="success"
          message={`匯入完成：新增 ${result.created} 筆，更新 ${result.updated} 筆`}
          showIcon closable onClose={() => setResult(null)}
          style={{ marginBottom: 12 }}
        />
      )}
      <Input
        placeholder="搜尋代號 / 簡稱 / 發行人"
        prefix={<SearchOutlined />}
        value={search}
        onChange={e => setSearch(e.target.value)}
        allowClear
        style={{ marginBottom: 12 }}
      />
      <Table
        rowKey="securities_code"
        dataSource={filtered}
        columns={columns}
        loading={loading}
        size="small"
        scroll={{ y: 400 }}
        pagination={{ pageSize: 50, showSizeChanger: false, showTotal: t => `共 ${t} 筆` }}
        rowSelection={{
          selectedRowKeys: selectedKeys,
          onChange: setSelectedKeys,
          getCheckboxProps: () => ({}),
        }}
      />
    </Modal>
  );
}
