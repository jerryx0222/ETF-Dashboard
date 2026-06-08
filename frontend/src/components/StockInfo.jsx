import React, { useEffect, useState } from 'react';
import {
  Layout, Table, Input, Select, Typography, Drawer, Descriptions, Tag, Spin, Space, Button
} from 'antd';
import { SearchOutlined, PlusOutlined } from '@ant-design/icons';
import api from '../api/axios';
import ImportModal from './ImportModal';

const { Content } = Layout;
const { Title } = Typography;
const { Option } = Select;

const dividendColumns = [
  { title: '除息日', dataIndex: 'ex_dividend_date', key: 'ex_dividend_date' },
  { title: '配息金額 (元)', dataIndex: 'dividend_amount', key: 'dividend_amount' },
  { title: '除息日收盤價 (元)', dataIndex: 'closing_price', key: 'closing_price' },
];

const frequencyColors = {
  monthly: 'blue',
  quarterly: 'green',
  semi_annual: 'orange',
  annual: 'red',
};

export default function StockInfo() {
  const [etfs, setEtfs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const [frequencyFilter, setFrequencyFilter] = useState('');
  const [selected, setSelected] = useState(null);
  const [drawerOpen, setDrawerOpen] = useState(false);
  const [importOpen, setImportOpen] = useState(false);

  useEffect(() => {
    fetchETFs();
  }, [search, frequencyFilter]);

  const fetchETFs = async () => {
    setLoading(true);
    try {
      const params = {};
      if (search) params.search = search;
      if (frequencyFilter) params.dividend_frequency = frequencyFilter;
      const res = await api.get('/etfs/', { params });
      setEtfs(res.data.results || res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const openDetail = async (record) => {
    try {
      const res = await api.get(`/etfs/${record.id}/`);
      setSelected(res.data);
      setDrawerOpen(true);
    } catch (err) {
      console.error(err);
    }
  };

  const columns = [
    { title: '證券代號', dataIndex: 'securities_code', key: 'securities_code', width: 100 },
    { title: '證券簡稱', dataIndex: 'securities_abbreviation', key: 'securities_abbreviation', width: 150 },
    { title: '發行人', dataIndex: 'issuer', key: 'issuer', width: 150 },
    { title: '標的指數', dataIndex: 'target_index', key: 'target_index', ellipsis: true },
    { title: '經理費(%)', dataIndex: 'management_fee', key: 'management_fee', width: 100 },
    { title: '保管費(%)', dataIndex: 'custody_fee', key: 'custody_fee', width: 100 },
    {
      title: '配息頻率',
      dataIndex: 'dividend_frequency',
      key: 'dividend_frequency',
      width: 100,
      render: (val, row) => (
        <Tag color={frequencyColors[val] || 'default'}>{row.dividend_frequency_display}</Tag>
      ),
    },
    { title: '配息銀行', dataIndex: 'dividend_bank', key: 'dividend_bank', width: 130 },
  ];

  return (
    <Layout style={{ minHeight: 'calc(100vh - 64px)', background: '#f5f5f5' }}>
      <Content style={{ padding: 24 }}>
        <Title level={3} style={{ marginBottom: 16 }}>股票資訊</Title>
        <Space style={{ marginBottom: 16 }} wrap>
          <Input
            placeholder="搜尋證券代號 / 簡稱 / 發行人"
            prefix={<SearchOutlined />}
            value={search}
            onChange={e => setSearch(e.target.value)}
            style={{ width: 280 }}
            allowClear
          />
          <Select
            placeholder="配息頻率"
            value={frequencyFilter || undefined}
            onChange={val => setFrequencyFilter(val || '')}
            style={{ width: 140 }}
            allowClear
          >
            <Option value="monthly">每月</Option>
            <Option value="quarterly">每季</Option>
            <Option value="semi_annual">每半年</Option>
            <Option value="annual">每年</Option>
          </Select>
          <Button
            type="primary"
            icon={<PlusOutlined />}
            onClick={() => setImportOpen(true)}
          >
            新增
          </Button>
        </Space>
        <Spin spinning={loading}>
          <Table
            dataSource={etfs}
            columns={columns}
            rowKey="id"
            onRow={record => ({ onClick: () => openDetail(record), style: { cursor: 'pointer' } })}
            pagination={{ pageSize: 20, showSizeChanger: false }}
            scroll={{ x: 900 }}
          />
        </Spin>

        <Drawer
          title={selected ? `${selected.securities_code} ${selected.securities_abbreviation}` : ''}
          open={drawerOpen}
          onClose={() => setDrawerOpen(false)}
          width={640}
        >
          {selected && (
            <>
              <Descriptions bordered column={1} size="small" style={{ marginBottom: 24 }}>
                <Descriptions.Item label="證券代號">{selected.securities_code}</Descriptions.Item>
                <Descriptions.Item label="證券簡稱">{selected.securities_abbreviation}</Descriptions.Item>
                <Descriptions.Item label="發行人">{selected.issuer}</Descriptions.Item>
                <Descriptions.Item label="標的指數">{selected.target_index}</Descriptions.Item>
                <Descriptions.Item label="經理費(%)">{selected.management_fee}</Descriptions.Item>
                <Descriptions.Item label="保管費(%)">{selected.custody_fee}</Descriptions.Item>
                <Descriptions.Item label="配息頻率">
                  <Tag color={frequencyColors[selected.dividend_frequency]}>
                    {selected.dividend_frequency_display}
                  </Tag>
                </Descriptions.Item>
                <Descriptions.Item label="配息銀行">{selected.dividend_bank}</Descriptions.Item>
              </Descriptions>
              <Title level={5}>歷史配息紀錄</Title>
              <Table
                dataSource={selected.dividend_records}
                columns={dividendColumns}
                rowKey="id"
                size="small"
                pagination={{ pageSize: 10 }}
              />
            </>
          )}
        </Drawer>

        <ImportModal
          open={importOpen}
          onClose={() => setImportOpen(false)}
          onImported={fetchETFs}
        />
      </Content>
    </Layout>
  );
}
