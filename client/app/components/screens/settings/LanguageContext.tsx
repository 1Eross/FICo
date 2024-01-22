// LanguageContext.tsx

import React, { createContext, useContext, FC, ReactNode, useState } from 'react';

type LanguageContextProps = {
  language: 'en' | 'ru';
  setLanguage: (language: 'en' | 'ru') => void;
};

const LanguageContext = createContext<LanguageContextProps | undefined>(undefined);

export const LanguageProvider: FC<{ children: ReactNode }> = ({ children }) => {
  const [language, setLanguage] = useState<'en' | 'ru'>('en');

  return (
    <LanguageContext.Provider value={{ language, setLanguage }}>
      {children}
    </LanguageContext.Provider>
  );
};

export const useLanguage = () => {
  const context = useContext(LanguageContext);
  if (!context) {
    throw new Error('useLanguage must be used within a LanguageProvider');
  }
  return context;
};
