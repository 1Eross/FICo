// AuthFields.tsx
import { FC } from 'react';
import { Text, TextInput, View } from 'react-native';
import { Control, Controller } from 'react-hook-form';
import cn from 'clsx';
import { IAuthFormData } from '@/types/auth.interface';

interface AuthFieldsProps {
  control: Control<IAuthFormData>;
  isRegistration: boolean;
}

const AuthFields: FC<AuthFieldsProps> = ({ control, isRegistration }) => {
  return (
    <>
      <Controller 
        control={control} 
        name='login' 
        rules={{
          required: 'Login is required',
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
                placeholder='Enter login'
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

      {isRegistration && (
        <>
          <Controller 
            control={control} 
            name='password'
            rules={{
              required: 'Password is required',
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
                    placeholder='Enter password'
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
        </>
      )}
    </>
  );
};

export default AuthFields;
