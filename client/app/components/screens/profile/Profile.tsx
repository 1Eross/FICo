import { FC } from 'react'
import { Text, View } from 'react-native'

import Layout from '@/components/ui/layout/Layout'
import Button from '@/components/ui/layout/bottom-menu/Button'
import { useAuth } from '@/hooks/useAuth'
import React from 'react'

const Profile: FC = () => {
    const{setUser} = useAuth() 

    return (
        <><View>
            <Text>Profile</Text>
        </View><Layout title='Profile'>
                <Button onPress={() => setUser(null)}>
                    Logout
                </Button>
            </Layout></>


    )
}

export default Profile