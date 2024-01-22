import React, { FC, useState } from 'react';
import { Pressable, Keyboard, Text, TouchableWithoutFeedback, View } from 'react-native';
import { Controller, SubmitHandler, useForm } from 'react-hook-form';
import { IAuthFormData } from '@/types/auth.interface';
import { useAuth } from '@/hooks/useAuth';
import Loader from '@/components/ui/layout/bottom-menu/loader';
import Button from '@/components/ui/layout/bottom-menu/Button';
import AuthFields from '@/components/screens/auth/AuthFields';
import { useLanguage } from '@/components/screens/settings/LanguageContext';  
import axios from 'axios';
import enStrings from '@/components/screens/auth/en.json'; // Укажите правильный путь к вашим файлам
import ruStrings from '@/components/screens/auth/ru.json';

const Auth: FC = () => {
  const [isReg, setIsReg] = useState(false);

  const { control, reset, handleSubmit } = useForm<IAuthFormData>({
    mode: 'onChange'
  });

  const { setUser } = useAuth();
  const { language, setLanguage } = useLanguage();

  const onSubmit: SubmitHandler<IAuthFormData> = data => {
    setUser({
      _id: '',
      ...data
    });
    reset();
  };

  const isLoading = false;

  const toggleLanguage = () => {
    const newLanguage = language === 'ru' ? 'en' : 'ru';
    setLanguage(newLanguage);
  };

  return (
    <TouchableWithoutFeedback onPress={Keyboard.dismiss} accessible={false}>
      <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
        <View style={{ width: '75%' }}>
          <Text style={{ color: 'white', fontSize: 30, fontWeight: 'bold', textAlign: 'center', marginBottom: 20 }}>
            {language === 'en' ? (isReg ? enStrings.signUp : enStrings.In) : (isReg ? ruStrings.signUp : ruStrings.In)}
          </Text>

          {isLoading ? (
            <Loader /> 
          ) : (
            <>
              <AuthFields control={control} isRegistration={isReg} />

              <Button onPress={handleSubmit(onSubmit)}>
                {language === 'en' ? (isReg ? enStrings.signUp : enStrings.signIn) : (isReg ? ruStrings.signUp : ruStrings.signIn)}
              </Button>

              <Pressable 
                onPress={() => setIsReg(!isReg)} 
                style={{ width: '55%', alignSelf: 'flex-end' }}
              >
                <Text style={{ color: 'white', fontSize: 16, textAlign: 'right', marginTop: 10 }}>
                  {language === 'en' ? (isReg ? enStrings.signIn : enStrings.signUp) : (isReg ? ruStrings.signIn : ruStrings.signUp)}
                </Text>
              </Pressable>
            </>
          )}
        </View>

        <Pressable 
          onPress={toggleLanguage} 
          style={{ position: 'absolute', top: 50, right: 20, backgroundColor: '#272541', borderRadius: 10, padding: 10 }}
        >
          <Text style={{ color: 'white', fontSize: 18 }}>
            {language === 'en' ? enStrings.changeLanguage : ruStrings.changeLanguage}
          </Text>
        </Pressable>
      </View>
    </TouchableWithoutFeedback>
  );
};

export default Auth;