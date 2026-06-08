import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { Menu, Layout, Space, Typography, Button } from 'antd';
import { StockOutlined, DownloadOutlined, LogoutOutlined, UserOutlined } from '@ant-design/icons';
import { useAuth } from '../context/AuthContext';

const { Header } = Layout;
const { Text } = Typography;

const menuItems = [
  { key: '/stock-info', icon: <StockOutlined />, label: '股票資訊' },
  { key: '/download', icon: <DownloadOutlined />, label: '下載資料' },
];

export default function Navbar() {
  const navigate = useNavigate();
  const location = useLocation();
  const { user, logout } = useAuth();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <Header style={{ display: 'flex', alignItems: 'center', padding: '0 24px' }}>
      <div style={{ color: '#fff', fontSize: 18, fontWeight: 700, marginRight: 40, whiteSpace: 'nowrap' }}>
        ETF Dashboard
      </div>
      <Menu
        theme="dark"
        mode="horizontal"
        selectedKeys={[location.pathname]}
        items={menuItems}
        onClick={({ key }) => navigate(key)}
        style={{ flex: 1, minWidth: 0 }}
      />
      <Space style={{ marginLeft: 24 }}>
        <UserOutlined style={{ color: '#fff' }} />
        <Text style={{ color: '#fff' }}>{user}</Text>
        <Button
          type="text"
          icon={<LogoutOutlined />}
          style={{ color: '#fff' }}
          onClick={handleLogout}
        >
          登出
        </Button>
      </Space>
    </Header>
  );
}
