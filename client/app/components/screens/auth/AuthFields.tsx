// AuthFields.tsx
import React, { FC } from 'react';
import { Text, TextInput, View } from 'react-native';
import { Control, Controller } from 'react-hook-form';
import cn from 'clsx';
import { IAuthFormData } from '@/types/auth.interface';
import { validEmail } from '@/components/screens/auth/email.rgx';
import { useLanguage } from '@/components/screens/settings/LanguageContext';
import enStrings from '@/components/screens/auth/en.json'; // Укажите правильный путь к вашим файлам
import ruStrings from '@/components/screens/auth/ru.json';

interface AuthFieldsProps {
  control: Control<IAuthFormData>;
  isRegistration: boolean;
}

const AuthFields: FC<AuthFieldsProps> = ({ control, isRegistration }) => {
  const { language } = useLanguage();

  return (
    <>
      {isRegistration && (
        <>
          <Controller 
            control={control} 
            name='firstName'
            rules={{
              required: language === 'en' ? enStrings.enterFirstName : ruStrings.enterFirstName,
            }} 
            render={({ 
              field: { value, onChange, onBlur }, 
              fieldState: { error }
            }) => (
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
                    value={value} 
                    onChangeText={onChange} 
                    onBlur={onBlur} 
                    autoCapitalize='words'
                    className='text-white text-lg'
                  />
                </View>
                {error && <Text className='text-red-500'>{error.message}</Text>}
              </>
            )}
          />

          <Controller 
            control={control} 
            name='lastName'
            rules={{
              required: language === 'en' ? enStrings.enterLastName : ruStrings.enterLastName,
            }} 
            render={({ 
              field: { value, onChange, onBlur }, 
              fieldState: { error }
            }) => (
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
                    value={value} 
                    onChangeText={onChange} 
                    onBlur={onBlur} 
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
        control={control} 
        name='login' 
        rules={{
          required: language === 'en' ? enStrings.enterLogin : ruStrings.enterLogin,
        }} 
        render={({ 
          field: { value, onChange, onBlur }, 
          fieldState: { error }
        }) => (
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
                value={value} 
                onChangeText={onChange} 
                onBlur={onBlur} 
                autoCapitalize='none'
                className='text-white text-lg'
              />
            </View>
            {error && <Text className='text-red-500'>{error.message}</Text>}
          </>
        )}
      />

      <Controller 
        control={control} 
        name='password'
        rules={{
          required: language === 'en' ? enStrings.enterPassword : ruStrings.enterPassword,
        }} 
        render={({ 
          field: { value, onChange, onBlur }, 
          fieldState: { error }
        }) => (
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
                value={value} 
                onChangeText={onChange} 
                onBlur={onBlur} 
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
            control={control} 
            name='email'
            rules={{
              required: language === 'en' ? enStrings.enterEmail : ruStrings.enterEmail,
              pattern: {
                value: validEmail,
                message: language === 'en' ? enStrings.invalidEmail : ruStrings.invalidEmail,
              },
            }} 
            render={({ 
              field: { value, onChange, onBlur }, 
              fieldState: { error }
            }) => (
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
                    value={value} 
                    onChangeText={onChange} 
                    onBlur={onBlur} 
                    autoCapitalize='none'
                    className='text-white text-lg'
                  />
                </View>
                {error && <Text className='text-red-500'>{error.message}</Text>}
              </>
            )}
          />

          <Controller 
            control={control} 
            name='phoneNumber'
            rules={{
              required: language === 'en' ? enStrings.enterPhoneNumber : ruStrings.enterPhoneNumber,
              pattern: {
                value: /^\+?[7-9][0-9]{0,10}$/,
                message: language === 'en' ? enStrings.invalidPhoneNumber : ruStrings.invalidPhoneNumber,
              },
            }} 
            render={({ 
              field: { value, onChange, onBlur }, 
              fieldState: { error }
            }) => (
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
                    value={value} 
                    onChangeText={onChange} 
                    onBlur={onBlur} 
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
    </>
  );
};

export default AuthFields;
