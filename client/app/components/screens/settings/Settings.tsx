import React, { FC } from 'react';
import { Text, View, Button as RNButton } from 'react-native';
import { useLanguage } from '@/components/screens/settings/LanguageContext';
import resources from '../../../../i18nResources';

const Settings: FC = () => {
    const { language, setLanguage } = useLanguage();
  
    const switchLanguage = () => {
      setLanguage((prevLanguage: 'en' | 'ru') => (prevLanguage === 'en' ? 'ru' : 'en'));
    };
  
    return (
      <View>
        <Text>{resources[language].settings}</Text>
        <RNButton title={resources[language].switchLanguage} onPress={switchLanguage} />
      </View>
    );
  };
  
  export default Settings;