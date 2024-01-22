// i18nResources.ts

interface ResourceLanguage {
    profile: string;
    exit: string;
    settings: string;
    switchLanguage: string;
  }
  
  interface Resources {
    en: ResourceLanguage;
    ru: ResourceLanguage;
  }
  
  const resources: Resources = {
    en: {
      profile: 'Profile',
      exit: 'Exit',
      settings: 'Settings',
      switchLanguage: 'Switch Language',
    },
    ru: {
      profile: 'Профиль',
      exit: 'Выйти',
      settings: 'Настройки',
      switchLanguage: 'Сменить язык',
    },
  };
  
  export default resources;
  