// Profile.tsx

import React, { FC } from 'react';
import { View, Text } from 'react-native';
import Layout from '@/components/ui/layout/Layout';
import Button from '@/components/ui/layout/bottom-menu/Button';
import { useAuth } from '@/hooks/useAuth';
import resources from '../../../../i18nResources';

const Profile: FC = () => {
    const { setUser } = useAuth();

    const language = 'ru'; // Здесь установите выбранный язык

    return (
        <Layout title={resources[language].profile}>
            <Button onPress={() => setUser(null)}>
                <View className='items-center justify-center flex-1'>
                </View>
                {resources[language].exit}
            </Button>
        </Layout>
    );
};

export default Profile;
