import React, { FC, useEffect, useState } from 'react';
import { Text, View, TextInput, Button } from 'react-native';

interface StatisticData {
  User_id: number; // Или замените тип на тот, который соответствует вашему gettedUser.id
}

const Statistics: FC = () => {
  const [statisticsData, setStatisticsData] = useState<StatisticData | null>(null);
  const [userLogin, setUserLogin] = useState<string>('');
  const [userPassword, setUserPassword] = useState<string>('');

  const fetchData = () => {
    // Замените URL на эндпоинт вашего сервера
    fetch(`http://192.168.43.91:5432/authorization?user_login=${userLogin}&user_password=${userPassword}`)
      .then(response => response.json())
      .then(data => {
        setStatisticsData(data);
      })
      .catch(error => console.error('Ошибка при получении данных с сервера:', error));
  };

  const sendDataToServer = () => {
    const jsonData = JSON.stringify({ user_login: userLogin, user_password: userPassword });

    // Замените URL на эндпоинт вашего сервера для отправки данных
    fetch('http://your-server-endpoint', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: jsonData,
    })
      .then(response => response.json())
      .then(data => {
        console.log('Данные успешно отправлены на сервер:', data);
        // Дополнительные действия, если необходимо
      })
      .catch(error => console.error('Ошибка при отправке данных на сервер:', error));
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
