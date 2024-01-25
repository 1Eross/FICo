import { FC, useState } from 'react';
import { Text, View, Image, TextInput, StyleSheet, Pressable } from 'react-native';
import Layout from '@/components/ui/layout/Layout';
import Button from '@/components/ui/layout/bottom-menu/Button';
import { useAuth } from '@/hooks/useAuth';
import { useLanguage } from '@/components/screens/settings/LanguageContext';
import React from 'react';

const Profile: FC = () => {
  const { setUser } = useAuth();
  const { language, setLanguage } = useLanguage();
  const [firstName, setFirstName] = useState('Иван');
  const [lastName, setLastName] = useState('Маремьянов');
  const [email, setEmail] = useState('john.doe@example.com');
  const [phoneNumber, setPhoneNumber] = useState('+1234567890');

  const handleLogout = () => {
    setUser(null);
  };

  const toggleLanguage = () => {
    const newLanguage = language === 'ru' ? 'en' : 'ru';
    setLanguage(newLanguage);
  };

  return (
    <Layout title={language === 'en' ? 'Profile' : 'Профиль'}>
      <View style={styles.profileContainer}>
        <View style={styles.avatarContainer}>
          {/* Add profile picture here */}
          <Image
            style={styles.avatar}
            source={require('@/components/screens/profile/user.png')}
          />
          <Text style={styles.editText}>{language === 'en' ? 'Edit' : 'Редактировать'}</Text>
        </View>

        <Text style={styles.nameText}>{firstName}</Text>
        <Text style={styles.nameText}>{lastName}</Text>

        <Text style={styles.labelText}>{language === 'en' ? 'Your email:' : 'Ваш email:'}</Text>
        <TextInput
          style={styles.input}
          value={email}
          onChangeText={(text) => setEmail(text)}
          placeholder={language === 'en' ? 'Email' : 'Эл. почта'}
        />

        <Text style={styles.labelText}>{language === 'en' ? 'Your phone number:' : 'Ваш номер телефона:'}</Text>
        <TextInput
          style={styles.input}
          value={phoneNumber}
          onChangeText={(text) => setPhoneNumber(text)}
          placeholder={language === 'en' ? 'Phone Number' : 'Номер телефона'}
        />

        <Button onPress={handleLogout}>
          {language === 'en' ? 'Logout' : 'Выйти'}
        </Button>

        <Pressable
          onPress={toggleLanguage}
          style={{
            position: 'absolute',
            top: 580,
            right: 10,
            backgroundColor: '#272541',
            borderRadius: 10,
            padding: 10,
          }}
        >
          <Text style={{ color: 'white', fontSize: 18 }}>
            {language === 'en' ? 'Change Language' : 'Изменить язык'}
          </Text>
        </Pressable>
      </View>
    </Layout>
  );
};

const styles = StyleSheet.create({
  profileContainer: {
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingTop: 20,
  },
  avatarContainer: {
    position: 'relative',
    marginBottom: 20,
  },
  avatar: {
    width: 150,
    height: 150,
    borderRadius: 50,
  },
  editText: {
    fontSize: 20,
    position: 'absolute',
    bottom: 0,
    right: 0,
    backgroundColor: 'lightblue',
    padding: 5,
    borderRadius: 10,
  },
  nameText: {
    fontSize: 22,
    color: 'white',
    marginBottom: 10,
  },
  labelText: {
    fontSize: 16,
    color: 'white',
    alignSelf: 'flex-start',
    marginBottom: 5,
  },
  input: {
    height: 40,
    borderColor: '#272541',
    borderWidth: 1,
    borderRadius: 5,
    marginBottom: 10,
    paddingLeft: 10,
    width: '100%',
    color: 'white',
  },
});

export default Profile;
