import React, { FC, useEffect, useState } from 'react';
import { View, Text, FlatList, SafeAreaView } from 'react-native';
import { BarChart } from 'react-native-chart-kit';

// Предположим, что у вас есть функция для получения данных из базы данных
const fetchUserDataFromDatabase = async () => {
  // Ваш код для получения данных из базы данных
  // Например, используйте асинхронный запрос к вашему API
  // Возвращайте объект данных пользователя
  // Например: return await fetch('ваш API endpoint').then((response) => response.json());
};

const categories = ['Transport', 'Health', 'Food', 'Technology', 'Entertainment'];

const Statistics: FC = () => {
  const [userData, setUserData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      // Загружаем данные пользователя из базы данных
      const userDatabaseData = await fetchUserDataFromDatabase();
      setUserData(userDatabaseData);
    };

    fetchData();
  }, []);

  const groupedData = userData.reduce((result, item) => {
    const key = `${item.date}-${item.category}`;
    result[key] = (result[key] || 0) + item.amount;
    return result;
  }, {});

  const chartData = Object.keys(groupedData).map((key) => ({
    date: key.split('-')[0],
    category: key.split('-')[1],
    amount: groupedData[key],
  }));

  return (
    <SafeAreaView style={{ flex: 1, backgroundColor: '#000' }}>
      <View style={{ flex: 1, paddingHorizontal: 16, paddingTop: 16 }}>
        {/* График по датам */}
        <BarChart
          data={{
            labels: chartData.map((item) => item.date),
            datasets: [
              {
                data: chartData.map((item) => item.amount),
              },
            ],
          }}
          width={400}
          height={200}
          yAxisLabel="₽"
          chartConfig={{
            backgroundGradientFrom: '#000',
            backgroundGradientTo: '#000',
            color: (opacity = 1) => `rgba(138, 43, 226, ${opacity})`, // фиолетовый цвет
            style: {
              borderRadius: 16,
            },
          }}
          style={{ marginVertical: 8 }}
        />

        {/* Список категорий с суммами */}
        <FlatList
          data={categories}
          keyExtractor={(item) => item}
          renderItem={({ item }) => (
            <View style={{ flexDirection: 'row', justifyContent: 'space-between', padding: 10 }}>
              <Text style={{ color: '#fff' }}>{item}</Text>
              <Text style={{ color: '#fff' }}>{groupedData[item] || 0} ₽</Text>
            </View>
          )}
        />
      </View>
    </SafeAreaView>
  );
};

export default Statistics;
