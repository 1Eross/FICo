import React, { FC, useEffect, useState } from 'react';
import { Text, View } from 'react-native';

interface StatisticData {
  User_id: number; // Или замените тип на тот, который соответствует вашему gettedUser.id
}

const Statistics: FC = () => {
  const [statisticsData, setStatisticsData] = useState<StatisticData | null>(null);

  useEffect(() => {
    // Замените URL на эндпоинт вашего сервера
    fetch('http://192.168.132.81:5434/authorization?user_login=zalupa123&user_password=12345678')
      .then(response => response.json())
      .then(data => {
        setStatisticsData(data);
      })
      .catch(error => console.error('Ошибка при получении данных с сервера:', error));
  }, []);

  return (
    <View>
      <Text>Statistics</Text>
      {statisticsData && (
        <View>
          <Text>User ID: {statisticsData.User_id}</Text>
        </View>
      )}
    </View>
  );
};

export default Statistics;
