// App.tsx

import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { SafeAreaProvider } from 'react-native-safe-area-context';
import AuthProvider from '@/providers/AuthProvider';
import Navigation from '@/navigation/Navigation';
import { LanguageProvider } from '@/components/screens/settings/LanguageContext';

const queryClient = new QueryClient();

export default function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <AuthProvider>
        <SafeAreaProvider>
          <LanguageProvider>
            <Navigation />
          </LanguageProvider>
        </SafeAreaProvider>
      </AuthProvider>
      <StatusBar style='light' />
    </QueryClientProvider>
  );
}
