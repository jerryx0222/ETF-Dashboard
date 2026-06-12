import React, { useEffect, useState } from 'react';
import {
  Layout, Table, Input, Select, Typography, Drawer, Descriptions, Tag, Spin, Space, Button,
  AutoComplete, message
} from 'antd';
import { SearchOutlined, PlusOutlined, EditOutlined, DownloadOutlined, FileExcelOutlined } from '@ant-design/icons';
import * as XLSX from 'xlsx';
import api from '../api/axios';
import ImportModal from './ImportModal';

const { Content } = Layout;
const { Title } = Typography;
const { Option } = Select;

const TAIWAN_BANKS = [
  '台灣銀行', '土地銀行', '合作金庫銀行', '第一銀行', '華南銀行',
  '彰化銀行', '兆豐銀行', '台灣企銀', '永豐銀行', '玉山銀行',
  '國泰世華銀行', '台北富邦銀行', '中國信託銀行', '台新銀行',
  '聯邦銀行', '遠東商銀', '元大銀行', '凱基銀行', '安泰銀行',
  '星展銀行', '滙豐銀行', '花旗銀行', '渣打銀行', '三信商銀',
  '京城銀行', '板信商銀', '台中商銀', '高雄銀行', '中華郵政',
  '農業金庫', '陽信商銀', '大眾商銀', '華泰銀行', '上海商銀',
  '台灣新光商銀', '日盛銀行', '瑞興銀行', '樂天銀行',
];

const dividendColumns = [
  { title: '除息日', dataIndex: 'ex_dividend_date', key: 'ex_dividend_date' },
  { title: '配息金額 (元)', dataIndex: 'dividend_amount', key: 'dividend_amount' },
  { title: '除息日收盤價 (元)', dataIndex: 'closing_price', key: 'closing_price' },
  {
    title: '現金殖利率',
    key: 'yield',
    render: (_, row) => {
      const price = parseFloat(row.closing_price);
      const amount = parseFloat(row.dividend_amount);
      if (!price) return '-';
      return `${((amount / price) * 100).toFixed(2)}%`;
    },
  },
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
  const [editingBank, setEditingBank] = useState(false);
  const [bankInput, setBankInput] = useState('');
  const [bankSaving, setBankSaving] = useState(false);
  const [dividendImporting, setDividendImporting] = useState(false);

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
      setEditingBank(false);
      setBankInput(res.data.dividend_bank || '');
      setDrawerOpen(true);
    } catch (err) {
      console.error(err);
    }
  };

  const exportDividendExcel = () => {
    if (!selected?.dividend_records?.length) return;
    const rows = selected.dividend_records.map(r => {
      const price = parseFloat(r.closing_price);
      const amount = parseFloat(r.dividend_amount);
      const yieldVal = price ? ((amount / price) * 100).toFixed(2) + '%' : '-';
      return {
        '除息日': r.ex_dividend_date,
        '配息金額 (元)': r.dividend_amount,
        '除息日收盤價 (元)': r.closing_price,
        '現金殖利率': yieldVal,
      };
    });
    const ws = XLSX.utils.json_to_sheet(rows);
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, '歷史配息紀錄');
    XLSX.writeFile(wb, `${selected.securities_code}_${selected.securities_abbreviation}_配息紀錄.xlsx`);
  };

  const importDividends = async () => {
    setDividendImporting(true);
    try {
      const res = await api.post(`/etfs/${selected.id}/import_dividends/`);
      message.success(`匯入完成：新增 ${res.data.created} 筆，更新 ${res.data.updated} 筆`);
      const detail = await api.get(`/etfs/${selected.id}/`);
      setSelected(detail.data);
    } catch (err) {
      message.error(err.response?.data?.error || '匯入失敗');
    } finally {
      setDividendImporting(false);
    }
  };

  const saveBank = async () => {
    setBankSaving(true);
    try {
      await api.patch(`/etfs/${selected.id}/`, { dividend_bank: bankInput });
      setSelected(prev => ({ ...prev, dividend_bank: bankInput }));
      setEditingBank(false);
      fetchETFs();
      message.success('配息銀行已更新');
    } catch (err) {
      message.error('儲存失敗');
    } finally {
      setBankSaving(false);
    }
  };

  const columns = [
    { title: '證券代號', dataIndex: 'securities_code', key: 'securities_code', width: 100 },
    { title: '證券簡稱', dataIndex: 'securities_abbreviation', key: 'securities_abbreviation', width: 150 },
    { title: '發行人', dataIndex: 'issuer', key: 'issuer', width: 150 },
    { title: '標的指數', dataIndex: 'target_index', key: 'target_index', ellipsis: true },
    {
      title: <span style={{ color: '#ff4d4f' }}>年化現金殖利率</span>,
      dataIndex: 'annualized_yield',
      key: 'annualized_yield',
      width: 140,
      render: (val) => val != null ? <span style={{ color: '#ff4d4f' }}>{val.toFixed(2)}%</span> : '',
    },
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
          onClose={() => { setDrawerOpen(false); setEditingBank(false); }}
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
                <Descriptions.Item label="配息銀行">
                  {editingBank ? (
                    <Space>
                      <AutoComplete
                        value={bankInput}
                        onChange={setBankInput}
                        options={TAIWAN_BANKS
                          .filter(b => !bankInput || b.includes(bankInput))
                          .map(b => ({ value: b }))}
                        style={{ width: 200 }}
                        placeholder="輸入關鍵字搜尋"
                        autoFocus
                      />
                      <Button type="primary" size="small" loading={bankSaving} onClick={saveBank}>儲存</Button>
                      <Button size="small" onClick={() => { setEditingBank(false); setBankInput(selected.dividend_bank || ''); }}>取消</Button>
                    </Space>
                  ) : (
                    <Space>
                      <span>{selected.dividend_bank || '-'}</span>
                      <Button type="link" size="small" icon={<EditOutlined />} onClick={() => setEditingBank(true)} />
                    </Space>
                  )}
                </Descriptions.Item>
              </Descriptions>
              <Space style={{ marginBottom: 8 }}>
                <Title level={5} style={{ margin: 0 }}>歷史配息紀錄</Title>
                <Button
                  size="small"
                  icon={<DownloadOutlined />}
                  loading={dividendImporting}
                  onClick={importDividends}
                >
                  匯入歷史配息紀錄
                </Button>
                <Button
                  size="small"
                  icon={<FileExcelOutlined />}
                  onClick={exportDividendExcel}
                  disabled={!selected?.dividend_records?.length}
                >
                  下載存成EXCEL檔
                </Button>
              </Space>
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
