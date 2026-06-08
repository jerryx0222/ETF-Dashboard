import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { ConfigProvider, Layout } from 'antd';
import zhTW from 'antd/locale/zh_TW';
import { AuthProvider, useAuth } from './context/AuthContext';
import Navbar from './components/Navbar';
import Login from './components/Login';
import StockInfo from './components/StockInfo';
import DownloadData from './components/DownloadData';

function ProtectedRoute({ children }) {
  const { user } = useAuth();
  return user ? children : <Navigate to="/login" replace />;
}

function AppRoutes() {
  const { user } = useAuth();
  return (
    <Routes>
      <Route path="/login" element={user ? <Navigate to="/stock-info" replace /> : <Login />} />
      <Route path="/" element={<Navigate to="/stock-info" replace />} />
      <Route
        path="/stock-info"
        element={
          <ProtectedRoute>
            <Layout style={{ minHeight: '100vh' }}>
              <Navbar />
              <StockInfo />
            </Layout>
          </ProtectedRoute>
        }
      />
      <Route
        path="/download"
        element={
          <ProtectedRoute>
            <Layout style={{ minHeight: '100vh' }}>
              <Navbar />
              <DownloadData />
            </Layout>
          </ProtectedRoute>
        }
      />
    </Routes>
  );
}

export default function App() {
  return (
    <ConfigProvider locale={zhTW}>
      <AuthProvider>
        <BrowserRouter>
          <AppRoutes />
        </BrowserRouter>
      </AuthProvider>
    </ConfigProvider>
  );
}
