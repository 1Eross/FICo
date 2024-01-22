import { FC } from 'react'
import { Text, View, StyleSheet, Image, TouchableOpacity } from 'react-native'
import { Control, Controller, useForm } from 'react-hook-form'
import Layout from '@/components/ui/layout/Layout'
import Button from '@/components/ui/layout/bottom-menu/Button'
import { useAuth } from '@/hooks/useAuth'
import ProfileFields from './ProfileFields'
import { IProfile } from '@/types/profile.interface'

const Profile: FC = () => {
    const{setUser} = useAuth() 
    const {control} = useForm<IProfile>({
    })
    return (
        <Layout title='Профиль'>
            <View style={styles.container}> 
            <Image style={styles.avatar} source={require('C:\Users\MSI\OneDrive\Рабочий стол\Avatar.jpg')} />
            <ProfileFields control={control}/>
            </View>
            <Button>Редактировать профиль</Button>
            <Button onPress={() => setUser(null)}>
                <View className='items-center justify-center flex-1'> 

                </View>
                Exit
            </Button>
        </Layout>
    )
    
}
const styles = StyleSheet.create({
    container: {
      flex: 1,
      padding: 16,
    },
    avatar: {
      width: 120,
      height: 120,
      borderRadius: 60,
      marginBottom: 16,
    },
    editButton: {
      backgroundColor: '',
      paddingVertical: 8,
      paddingHorizontal: 16,
      borderRadius: 8,
    },
    editButtonText: {
      color: 'white',
      fontWeight: 'bold',
    },
  });
export default Profile
