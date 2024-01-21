import { FC } from 'react'
import { Text, TextInput, View } from 'react-native'
import { Control, Controller, SubmitHandler, useForm } from 'react-hook-form'
import { validEmail } from '@/components/screens/auth/email.rgx'
import cn from 'clsx'
import { IAuthFormData } from '@/types/auth.interface'

const AuthFields: FC<{ control: Control<IAuthFormData> }> = ({ control }) => {
    return (
        <>
        <Controller 
                                control={control} 
                                name='email'
                                rules={{
                                    required: 'Email is required',
                                    pattern: {
                                        value: validEmail,
                                        message: 'Your Email is Invalid!'
                                    }

                                }} 
                                render={({ 
                                field:{value, onChange, onBlur}, 
                                fieldState: {error}
                            }) => (
                        <>
                        <View 
                            className={cn(
                                'rounded bg-[#272541] border pb-4 pt-2.5 px-4 my-2',
                                 !!error ? 'border-red-500' : 'border-transparent'
                            )}
                        >
                            <TextInput 
                                placeholder='Enter email'
                                placeholderTextColor ='#858585' 
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
                                    required: 'Password is required',
                                    minLength: {
                                        value: 6,
                                        message: 'Password should be min 6 symbols'
                                    }

                                }} 
                                render={({ 
                                field:{value, onChange, onBlur}, 
                                fieldState: {error}
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
                                placeholderTextColor ='#858585' 
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

    )
}
export default AuthFields