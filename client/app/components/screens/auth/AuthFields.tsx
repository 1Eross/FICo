// AuthFields.tsx
import React, { FC, useState } from 'react';
import { Text, TextInput, View, Button, Alert } from 'react-native';
import { Control, Controller, SubmitHandler, useForm } from 'react-hook-form';
import cn from 'clsx';
import axios from 'axios';
import { IAuthFormData } from '@/types/auth.interface';
import { validEmail } from '@/components/screens/auth/email.rgx';
import { useLanguage } from '@/components/screens/settings/LanguageContext';
import enStrings from '@/components/screens/auth/en.json';
import ruStrings from '@/components/screens/auth/ru.json';
import AsyncStorage from '@react-native-async-storage/async-storage';

interface AuthFieldsProps {
  control: Control<IAuthFormData>;
  isRegistration: boolean;
}

interface AuthRequestModel {
  login: string;
  password: string;
}

interface RegRequestModel {
  phoneNumber: any;
  login: string;
  password: string;
  firstName: string;
  email: string;
}

const AuthFields: FC<AuthFieldsProps> = ({ control, isRegistration }) => {
  const { language } = useLanguage();
  const [responseData, setResponseData] = useState<any | null>(null);
  const { handleSubmit, control: formControl } = useForm<IAuthFormData>();

  const handleSendRequest = async (data: AuthRequestModel) => {
    try {
      console.log(data.login, data.password)
      if (!data.login || !data.password) {
        // Проверка, что данные не пустые
        console.error('Invalid data:', data);
        Alert.alert('Error', 'Invalid data');
        return;
      }

      const url = isRegistration ? 'http://192.168.132.81:8080/reg' : 'http://192.168.132.81:8080/token';
  
      const requestData: AuthRequestModel = {
        login: data.login,
        password: data.password,
        ...(isRegistration && {
          FNameLName: (data as RegRequestModel).firstName,
          phone: (data as RegRequestModel).phoneNumber,
          email: (data as RegRequestModel).email,
        }),
      };

      console.log(isRegistration)
  
      const response = await axios.post(url, requestData);
      setResponseData(response.data);
      await AsyncStorage.setItem('access_token', response.data.access_token);

      console.log('Response from backend:', response.data);
    } catch (error) {
      console.error('Error sending request:', error);
      Alert.alert('Error', 'Failed to send request');
    }
  };
  const onSubmit: SubmitHandler<IAuthFormData> = async (data) => {
    try {
      console.log(data)
      await handleSendRequest(data);
    } catch (error) {
      console.error('Error submitting form:', error);
      Alert.alert('Error', 'Failed to submit form');
    }
  };

  return (
    <>
      {isRegistration && (
        <>
          <Controller
            control={formControl}
            name='firstName'
            rules={{
              required: language === 'en' ? enStrings.enterFirstName : ruStrings.enterFirstName,
            }}
            render={({ field, fieldState: { error } }) => (
              <>
                <View
                  className={cn(
                    'rounded bg-[#272541] border pb-4 pt-2.5 px-4 my-2',
                    !!error ? 'border-red-500' : 'border-transparent'
                  )}
                >
                  <TextInput
                    placeholder={isRegistration ? (language === 'en' ? enStrings.enterFirstName : ruStrings.enterFirstName) : ''}
                    placeholderTextColor='#858585'
                    value={field.value}
                    onChangeText={field.onChange}
                    onBlur={field.onBlur}
                    autoCapitalize='words'
                    className='text-white text-lg'
                  />
                </View>
                {error && <Text className='text-red-500'>{error.message}</Text>}
              </>
            )}
          />

          <Controller
            control={formControl}
            name='lastName'
            rules={{
              required: language === 'en' ? enStrings.enterLastName : ruStrings.enterLastName,
            }}
            render={({ field, fieldState: { error } }) => (
              <>
                <View
                  className={cn(
                    'rounded bg-[#272541] border pb-4 pt-2.5 px-4 my-2',
                    !!error ? 'border-red-500' : 'border-transparent'
                  )}
                >
                  <TextInput
                    placeholder={isRegistration ? (language === 'en' ? enStrings.enterLastName : ruStrings.enterLastName) : ''}
                    placeholderTextColor='#858585'
                    value={field.value}
                    onChangeText={field.onChange}
                    onBlur={field.onBlur}
                    autoCapitalize='words'
                    className='text-white text-lg'
                  />
                </View>
                {error && <Text className='text-red-500'>{error.message}</Text>}
              </>
            )}
          />
        </>
      )}

      <Controller
        control={formControl}
        name='login'
        rules={{
          required: language === 'en' ? enStrings.enterLogin : ruStrings.enterLogin,
        }}
        render={({ field, fieldState: { error } }) => (
          <>
            <View
              className={cn(
                'rounded bg-[#272541] border pb-4 pt-2.5 px-4 my-2',
                !!error ? 'border-red-500' : 'border-transparent'
              )}
            >
              <TextInput
                placeholder={language === 'en' ? enStrings.enterLogin : ruStrings.enterLogin}
                placeholderTextColor='#858585'
                value={field.value}
                onChangeText={field.onChange}
                onBlur={field.onBlur}
                autoCapitalize='none'
                className='text-white text-lg'
              />
            </View>
            {error && <Text className='text-red-500'>{error.message}</Text>}
          </>
        )}
      />

      <Controller
        control={formControl}
        name='password'
        rules={{
          required: language === 'en' ? enStrings.enterPassword : ruStrings.enterPassword,
        }}
        render={({ field, fieldState: { error } }) => (
          <>
            <View
              className={cn(
                'rounded bg-[#272541] border pb-4 pt-2.5 px-4 my-2',
                !!error ? 'border-red-500' : 'border-transparent'
              )}
            >
              <TextInput
                placeholder={language === 'en' ? enStrings.enterPassword : ruStrings.enterPassword}
                placeholderTextColor='#858585'
                value={field.value}
                onChangeText={field.onChange}
                onBlur={field.onBlur}
                autoCapitalize='none'
                className='text-white text-lg'
                secureTextEntry
              />
            </View>
            {error && <Text className='text-red-500'>{error.message}</Text>}
          </>
        )}
      />

      {isRegistration && (
        <>
          <Controller
            control={formControl}
            name='email'
            rules={{
              required: language === 'en' ? enStrings.enterEmail : ruStrings.enterEmail,
              pattern: {
                value: validEmail,
                message: language === 'en' ? enStrings.invalidEmail : ruStrings.invalidEmail,
              },
            }}
            render={({ field, fieldState: { error } }) => (
              <>
                <View
                  className={cn(
                    'rounded bg-[#272541] border pb-4 pt-2.5 px-4 my-2',
                    !!error ? 'border-red-500' : 'border-transparent'
                  )}
                >
                  <TextInput
                    placeholder={language === 'en' ? enStrings.enterEmail : ruStrings.enterEmail}
                    placeholderTextColor='#858585'
                    value={field.value}
                    onChangeText={field.onChange}
                    onBlur={field.onBlur}
                    autoCapitalize='none'
                    className='text-white text-lg'
                  />
                </View>
                {error && <Text className='text-red-500'>{error.message}</Text>}
              </>
            )}
          />

          <Controller
            control={formControl}
            name='phoneNumber'
            rules={{
              required: language === 'en' ? enStrings.enterPhoneNumber : ruStrings.enterPhoneNumber,
              pattern: {
                value: /^\+?[7-9][0-9]{0,10}$/,
                message: language === 'en' ? enStrings.invalidPhoneNumber : ruStrings.invalidPhoneNumber,
              },
            }}
            render={({ field, fieldState: { error } }) => (
              <>
                <View
                  className={cn(
                    'rounded bg-[#272541] border pb-4 pt-2.5 px-4 my-2',
                    !!error ? 'border-red-500' : 'border-transparent'
                  )}
                >
                  <TextInput
                    placeholder={language === 'en' ? enStrings.enterPhoneNumber : ruStrings.enterPhoneNumber}
                    placeholderTextColor='#858585'
                    value={field.value}
                    onChangeText={field.onChange}
                    onBlur={field.onBlur}
                    keyboardType='phone-pad'
                    maxLength={11} // Ограничение на ввод (+7XXXXXXXXXX)
                    className='text-white text-lg'
                  />
                </View>
                {error && <Text className='text-red-500'>{error.message}</Text>}
              </>
            )}
          />
        </>
      )}

      <Button
        title="Send Request"
        onPress={handleSubmit(onSubmit)}
      />
    </>
  );
};

export default AuthFields;
