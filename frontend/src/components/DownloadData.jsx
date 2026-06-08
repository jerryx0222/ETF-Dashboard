import React, { useState } from 'react';
import { Layout, Card, Button, Typography, Space, Alert, Divider } from 'antd';
import { DownloadOutlined, FileExcelOutlined } from '@ant-design/icons';

const { Content } = Layout;
const { Title, Paragraph, Text } = Typography;

export default function DownloadData() {
  const [downloading, setDownloading] = useState(false);
  const [error, setError] = useState('');

  const handleDownloadExcel = async () => {
    setDownloading(true);
    setError('');
    try {
      const token = localStorage.getItem('access_token');
      const response = await fetch('/api/export/excel/', {
        headers: token ? { Authorization: `Bearer ${token}` } : {},
      });
      if (!response.ok) throw new Error('下載失敗，請稍後再試');
      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'etf_data.xlsx';
      a.click();
      window.URL.revokeObjectURL(url);
    } catch (err) {
      setError(err.message);
    } finally {
      setDownloading(false);
    }
  };

  return (
    <Layout style={{ minHeight: 'calc(100vh - 64px)', background: '#f5f5f5' }}>
      <Content style={{ padding: 24, maxWidth: 800, margin: '0 auto', width: '100%' }}>
        <Title level={3} style={{ marginBottom: 24 }}>下載資料</Title>

        {error && (
          <Alert type="error" message={error} showIcon style={{ marginBottom: 16 }} closable onClose={() => setError('')} />
        )}

        <Card>
          <Space direction="vertical" size="large" style={{ width: '100%' }}>
            <div>
              <Title level={5}>
                <FileExcelOutlined style={{ color: '#217346', marginRight: 8 }} />
                ETF 完整資料 (Excel)
              </Title>
              <Paragraph type="secondary">
                包含以下兩個工作表：
              </Paragraph>
              <ul style={{ paddingLeft: 20 }}>
                <li><Text>ETF基本資料 — 證券簡稱、代號、發行人、標的指數、經理費、保管費、配息頻率、配息銀行</Text></li>
                <li><Text>歷史配息紀錄 — 除息日、配息金額、除息日收盤價</Text></li>
              </ul>
            </div>
            <Divider style={{ margin: '0' }} />
            <Button
              type="primary"
              icon={<DownloadOutlined />}
              size="large"
              loading={downloading}
              onClick={handleDownloadExcel}
            >
              下載 Excel (.xlsx)
            </Button>
          </Space>
        </Card>
      </Content>
    </Layout>
  );
}
