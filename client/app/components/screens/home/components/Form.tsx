

import React, { useEffect, useState } from 'react';
import { View, StyleSheet, TextInput, Image, TouchableOpacity, SafeAreaView } from 'react-native';
import { Formik } from 'formik';
import { Picker } from '@react-native-picker/picker';
import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';
import MaskedInput from 'react-text-mask'


const Form = ({addCard}) => {
    const [cards, setCards] = useState([]);
    
    useEffect(() => {
        const loadCards = async () => {
          try {
            // Получаем токен из AsyncStorage
            const token = await AsyncStorage.getItem('jwt_token');
            
            // Отправляем запрос на сервер, передавая токен в заголовках
            const response = await axios.get('http://ваш_сервер/путь_к_загрузке_карточек', {
              headers: {
                Authorization: `Bearer ${token}`,
              },
            });
    
            // Устанавливаем полученные карточки в состояние
            setCards(response.data);
          } catch (error) {
            console.error('Error loading cards:', error);
          }
        };
    
        // Вызываем функцию загрузки карточек при монтировании компонента
        loadCards();
      }, []); // Пустой массив зависимостей, чтобы useEffect сработал только при монтировании

interface BankAccount {
  accountID: number;
  balance: number;
  currency: string;
  userID: number
}

const getAllBankAccounts = async () => {
  try {
    // Получение токена из AsyncStorage
    const token = await AsyncStorage.getItem('access_token');

    if (!token) {
      console.error('Token not found in AsyncStorage');
      return;
    }

    // Установка токена в заголовок запроса
    axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    console.log("Token %s", token)
    // Выполнение запроса на получение всех bank_account
    const response = await axios.get<BankAccount[]>('http://192.168.132.81:8080/bank_accounts');

    // Вывод bank_account в консоль
    console.log('Bank Accounts:', response.data);
  } catch (error) {
    console.error('Error while fetching bank accounts:', error);
  }
};

// Вызов функции для получения всех bank_account
getAllBankAccounts();
    
    
    return (
        <SafeAreaView>
      <Formik
        initialValues={{ number: '', category: '', data: '' }}
        onSubmit={(values, action) => {
          addCard(values);
          action.resetForm();
          // Вызываем функцию получения всех bank_account при нажатии на кнопку
          getAllBankAccounts();
        }}
      >
        {(props) => (
          <View style={styles.ViewMain}>
            <View style={styles.View}>
              {/* Остальные компоненты формы */}
            </View>
            <TouchableOpacity onPress={props.handleSubmit}>
              <Image style={styles.buttonImage} source={require('../assets/okButton.png')} />
            </TouchableOpacity>
          </View>
        )}
      </Formik>
    </SafeAreaView>
  );
};
        // <SafeAreaView>
        //     <Formik initialValues={{number: '', category: '', data: ''}} onSubmit={(values, action) => {addCard(values), action.resetForm}}>
        //         {(props) => (
        //             <View style={styles.ViewMain}>
        //                 <View style={styles.View}>
        //                     <TextInput
        //                         style={styles.input}
        //                         value={props.values.number}
        //                         keyboardType={'numeric'}
        //                         placeholder='Введите сумму'
        //                         placeholderTextColor='#664efe'
        //                         onChangeText={props.handleChange('number')}>
        //                     </TextInput> 
        //                     <Picker style={styles.picker} selectedValue={props.values.category} onValueChange={props.handleChange('category')}>
        //                         <Picker.Item label="" value="" />
        //                         <Picker.Item label="Учёба" value="Учёба" />
        //                         <Picker.Item label="Семья" value="Семья" />
        //                         <Picker.Item label="Здоровье" value="Здоровье" />
        //                         <Picker.Item label="Продукты" value="Продукты" />
        //                         <Picker.Item label="Кафе" value="Кафе" />
        //                         <Picker.Item label="Досуг" value="Досуг" />
        //                         <Picker.Item label="Транспорт" value="Транспорт" />
        //                         <Picker.Item label="Подарки" value="Подарки" />
        //                         <Picker.Item label="Покупки" value="Покупки" />
        //                     </Picker>
        //                     {/* <MaskedInput
        //                         style={styles.input}
        //                         mask={[/\d/, /\d/, /\d/, /\d/, '-', /\d/, /\d/, '-', /\d/, /\d/]}
        //                         placeholder='YYYY-MM-DD'
        //                         value={props.values.data}
        //                         onChange={props.handleChange('data')}>
        //                     </MaskedInput> */}
        //                     <TextInput
        //                         style={styles.input}
        //                         value={props.values.data}
        //                         keyboardType={'numeric'}
        //                         placeholder='YYYY-MM-DD'
        //                         placeholderTextColor='#664efe'
        //                         onChangeText={props.handleChange('data')}>
        //                     </TextInput>
        //                 </View>
        //                     <TouchableOpacity onPress={props.handleSubmit}>
        //                         <Image 
        //                             style={styles.buttonImage} 
        //                             source={require('../assets/okButton.png')}
        //                         />
        //                     </TouchableOpacity>
        //             </View>
        //         )}
        //     </Formik>
        // </SafeAreaView>
//     )
// }

const styles = StyleSheet.create({
    ViewMain: {
        backgroundColor: '#1c1c2e',
        justifyContent: 'center',
        alignItems: 'center',
    },
    View: {
        backgroundColor: '#1c1c2e'
    },
    input: {
        borderWidth: 1,
        marginTop: 15,
        padding: 10,
        borderColor: '#664efe',
        borderRadius: 10,
        fontSize: 20,
        color: '#664efe',
        backgroundColor: '#1c1c2e',
    },
    picker: {
        borderWidth: 1,
        marginTop: 15,
        padding: 10,
        borderColor: '#664efe',
        borderRadius: 10,
        fontSize: 20,
        color: '#664efe',
        backgroundColor: '#1c1c2e',
    },
    buttonImage: {
        width: 60,
        height: 60,
        
    },
})

export default Form