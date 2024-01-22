import React, { FC, useEffect, useState } from 'react';
import { Text, View, TextInput, Button } from 'react-native';

interface StatisticData {
  User_id: number; // Или замените тип на тот, который соответствует вашему gettedUser.id
}
interface TokenRequest {
  username: string;
  password: string;
}
const Statistics: FC = () => {
  const [statisticsData, setStatisticsData] = useState<StatisticData | null>(null);
  const [userLogin, setUserLogin] = useState<string>('');
  const [userPassword, setUserPassword] = useState<string>('');

  const fetchData = async () => {
    try {
      // Замените URL на эндпоинт вашего сервера
      const response = await fetch(`http://192.168.43.91:5432/authorization?user_login=${userLogin}&user_password=${userPassword}`);
      const data = await response.json();
      setStatisticsData(data);
    } catch (error) {
      console.error('Ошибка при получении данных с сервера:', error);
    }
  };

  const sendDataToServer = async () => {
    const jsonData: TokenRequest = {
      username: userLogin,
      password: userPassword
    };
    try {
      // Замените URL на эндпоинт вашего сервера для отправки данных
      const response = await fetch('https://wm7di4-188-162-229-242.ru.tuna.am/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(jsonData),
      });
      const data = await response;
      // const data = await response.json();
      console.log('Данные успешно отправлены на сервер:', data);
      // Дополнительные действия, если необходимо
    } catch (error) {
      console.error('Ошибка при отправке данных на сервер:', error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <View>
      <Text>Statistics</Text>
      
      {/* Ввод данных от пользователя */}
      <TextInput
        placeholder="Введите логин"
        value={userLogin}
        onChangeText={(text) => setUserLogin(text)}
      />
      <TextInput
        placeholder="Введите пароль"
        secureTextEntry
        value={userPassword}
        onChangeText={(text) => setUserPassword(text)}
      />
      <Button title="Отправить данные" onPress={sendDataToServer} />

      {/* Отображение статистики */}
      {statisticsData && (
        <View>
          <Text>User ID: {statisticsData.User_id}</Text>
        </View>
      )}
    </View>
  );
};

export default Statistics;