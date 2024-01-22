// Auth.tsx
import { FC, useState } from 'react';
import { Pressable, Keyboard, Text, TouchableWithoutFeedback, View } from 'react-native';
import { Controller, SubmitHandler, useForm } from 'react-hook-form';
import { IAuthFormData } from '@/types/auth.interface';
import { useAuth } from '@/hooks/useAuth';
import Loader from '@/components/ui/layout/bottom-menu/loader';
import Button from '@/components/ui/layout/bottom-menu/Button';
import cn from 'clsx';
import AuthFields from '@/components/screens/auth/AuthFields';

const Auth: FC = () => {
  const [isReg, setIsReg] = useState(false);

  const { control, reset, handleSubmit } = useForm<IAuthFormData>({
    mode: 'onChange'
  });

  const { setUser } = useAuth();

  const onSubmit: SubmitHandler<IAuthFormData> = data => {
    setUser({
      _id: '',
      ...data
    });
    reset();
  };

  const isLoading = false;

  return (
    <TouchableWithoutFeedback onPress={Keyboard.dismiss} accessible={false}>
      <View className='items-center justify-center flex-1'>
        <View className='w-3/4'>
          <Text className='text-white text-5xl fond-bold text-center mb-5'>
            {isReg ? 'Sign up' : 'Sign in'}
          </Text>

          {isLoading ? (
            <Loader /> 
          ) : (
            <>
              <AuthFields control={control} isRegistration={isReg} />

              <Button onPress={handleSubmit(onSubmit)}>Let's go</Button>

              <Pressable 
                onPress={() => setIsReg(!isReg)} 
                className='w-16 self-end'
              >
                <Text className='text-opacity-60 text-white text-base mt-3 text-right' >
                  {isReg ? 'Login' : 'Register'}
                </Text>
              </Pressable>
            </> 
          )}
        </View>
      </View>
    </TouchableWithoutFeedback>
  );
};

export default Auth;
