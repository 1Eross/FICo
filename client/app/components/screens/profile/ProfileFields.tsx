import { FC } from 'react'
import { Text, TextInput, View } from 'react-native'
import { Control, Controller, } from 'react-hook-form'
import { validEmail } from '@/components/screens/auth/email.rgx'
import cn from 'clsx'
import { IProfile } from '@/types/profile.interface'

const ProfileFields: FC<{ control: Control<IProfile> }> = ({ control }) => {
    return (
        <>
        <Text className='text-2xl'>Ваше имя</Text>
        <Controller 
            control={control} 
            name='name'
            render={({ 
                field:{value, onChange, onBlur}, 
                fieldState: {error}
            }) => (
            <View 
                className={cn(
                'rounded bg-[#272541] border pb-4 pt-2.5 px-4 my-2',
                )}
            >
            </View>
            )}
        />   
        <Text className='text-2xl'>Ваша почта</Text>
        <Controller 
            control={control} 
            name='email'
            render={({ 
                field:{value, onChange, onBlur}, 
                fieldState: {error}
            }) => (
            <View 
                className={cn(
                'rounded bg-[#272541] border pb-4 pt-2.5 px-4 my-2',
                )}
            >
            </View>
            )}
        />
                <Text className='text-2xl'>О себе</Text>
        <Controller 
            control={control} 
            name='words'
            render={({ 
                field:{value, onChange, onBlur}, 
                fieldState: {error}
            }) => (
            <View 
                className={cn(
                'rounded bg-[#272541] border pb-4 pt-2.5 px-4 my-2',
                )}
            >
            </View>
            )}
        />
        <Text className='text-2xl'>Ваш номер телефона</Text>
        <Controller 
            control={control} 
            name='phone'
            render={({ 
                field:{value, onChange, onBlur}, 
                fieldState: {error}
            }) => (
            <View 
                className={cn(
                'rounded bg-[#272541] border pb-4 pt-2.5 px-4 my-2',
                )}
            >
            </View>
            )}
        />       
        </>
        
    )
}
export default ProfileFields