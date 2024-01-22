// LanguageContext.tsx
import React, { createContext, useContext, ReactNode, useState, FC } from 'react';

type Language = 'en' | 'ru';

interface LanguageContextProps {
  children: ReactNode;
}

interface LanguageContextValue {
  language: Language;
  setLanguage: (lang: Language) => void;
}

const LanguageContext = createContext<LanguageContextValue | undefined>(undefined);

export const LanguageProvider: FC<LanguageContextProps> = ({ children }) => {
  const [language, setLanguage] = useState<Language>('en');

  const value: LanguageContextValue = {
    language,
    setLanguage,
  };

  return <LanguageContext.Provider value={value}>{children}</LanguageContext.Provider>;
};

export const useLanguage = () => {
  const context = useContext(LanguageContext);
  if (!context) {
    throw new Error('useLanguage must be used within a LanguageProvider');
  }
  return context;
};
