import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Card, Form, Input, Button, Tabs, Alert, Typography } from 'antd';
import { UserOutlined, LockOutlined, MailOutlined } from '@ant-design/icons';
import axios from 'axios';
import { useAuth } from '../context/AuthContext';

const { Title } = Typography;

export default function Login() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const { saveAuth } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (values, isRegister) => {
    setLoading(true);
    setError('');
    try {
      const url = isRegister ? '/api/auth/register/' : '/api/auth/login/';
      const { data } = await axios.post(url, values);
      saveAuth(data);
      navigate('/stock-info');
    } catch (err) {
      setError(err.response?.data?.error || '操作失敗，請稍後再試');
    } finally {
      setLoading(false);
    }
  };

  const LoginForm = () => (
    <Form onFinish={(v) => handleSubmit(v, false)} layout="vertical" size="large">
      <Form.Item name="username" rules={[{ required: true, message: '請輸入帳號' }]}>
        <Input prefix={<UserOutlined />} placeholder="帳號" autoComplete="username" />
      </Form.Item>
      <Form.Item name="password" rules={[{ required: true, message: '請輸入密碼' }]}>
        <Input.Password prefix={<LockOutlined />} placeholder="密碼" autoComplete="current-password" />
      </Form.Item>
      <Form.Item>
        <Button type="primary" htmlType="submit" loading={loading} block>
          登入
        </Button>
      </Form.Item>
    </Form>
  );

  const RegisterForm = () => (
    <Form onFinish={(v) => handleSubmit(v, true)} layout="vertical" size="large">
      <Form.Item name="username" rules={[{ required: true, message: '請輸入帳號' }]}>
        <Input prefix={<UserOutlined />} placeholder="帳號" autoComplete="username" />
      </Form.Item>
      <Form.Item name="email" rules={[{ type: 'email', message: '請輸入有效的 Email' }]}>
        <Input prefix={<MailOutlined />} placeholder="Email（選填）" autoComplete="email" />
      </Form.Item>
      <Form.Item
        name="password"
        rules={[{ required: true, message: '請輸入密碼' }, { min: 6, message: '密碼至少 6 個字元' }]}
      >
        <Input.Password prefix={<LockOutlined />} placeholder="密碼（至少 6 個字元）" autoComplete="new-password" />
      </Form.Item>
      <Form.Item
        name="confirm"
        dependencies={['password']}
        rules={[
          { required: true, message: '請再次輸入密碼' },
          ({ getFieldValue }) => ({
            validator(_, value) {
              if (!value || getFieldValue('password') === value) return Promise.resolve();
              return Promise.reject(new Error('兩次密碼不一致'));
            },
          }),
        ]}
      >
        <Input.Password prefix={<LockOutlined />} placeholder="確認密碼" autoComplete="new-password" />
      </Form.Item>
      <Form.Item>
        <Button type="primary" htmlType="submit" loading={loading} block>
          註冊
        </Button>
      </Form.Item>
    </Form>
  );

  return (
    <div style={{
      minHeight: '100vh',
      background: '#f0f2f5',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
    }}>
      <Card style={{ width: 400, boxShadow: '0 4px 24px rgba(0,0,0,0.1)' }}>
        <Title level={3} style={{ textAlign: 'center', marginBottom: 24 }}>ETF Dashboard</Title>
        {error && <Alert type="error" message={error} showIcon style={{ marginBottom: 16 }} />}
        <Tabs
          centered
          defaultActiveKey="login"
          onChange={() => setError('')}
          items={[
            { key: 'login', label: '登入', children: <LoginForm /> },
            { key: 'register', label: '新增使用者', children: <RegisterForm /> },
          ]}
        />
      </Card>
    </div>
  );
}
