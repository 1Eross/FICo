import React, { useState} from 'react'
import { View } from 'my-app/components/Themed'
import { StyleSheet, Text, FlatList, } from 'react-native'

// const [CardsData, SetCard] = [
//     {
//         id: '1',
//         number: '1000',
//         category: 'Медицина',
//         data: '12/12/12',
//     },
//     {
//         id: '2',
//         number: '2400',
//         category: 'Развлечения',
//         data: '12/12/12',
//     },
//     {
//         id: '3',
//         number: '456',
//         category: 'Медицина',
//         data: '12/12/12',
//     },
//     {
//         id: '4',
//         number: '12345',
//         category: 'Транспорт',
//         data: '12/12/12',
//     },
//     {
//         id: '5',
//         number: '6550',
//         category: 'Продукты',
//         data: '12/12/12',
//     },
// ]

const [cards, setCards] = useState([
    {summa: '35', cat: 'Medicine', chislo: '21/06/23'},
    {summa: '41', cat: 'Auto', chislo: '18/06/23'},
    {summa: '99', cat: 'Kaif', chislo: '11/06/23'},
]);

// const Item = ({item}: any,) => (
//     <View style={styles.View}>
//         <Text style={styles.text1}> {item.number} </Text>
//         <Text style={styles.text2}> {item.category} </Text>
//         <Text style={styles.text3}> {item.data} </Text>

//     </View>
// )

const CardsList = () => {
    return (
            <FlatList 
            data={cards}
            renderItem={({item}) => (
                <View>
                <Text>{item.summa}</Text>
                <Text>{item.cat}</Text>
                <Text>{item.chislo}</Text>
                </View>
            )}>
            </FlatList>
    )
}

const styles = StyleSheet.create({
    text1: {
        fontSize: 25,
    },
    text2: {
        fontSize: 18,
    },
    text3: {
        fontSize: 15,
    },
    List: {
        backgroundColor: '#1c1c2e',
        width: '100%',
    },
    View: {
        backgroundColor: '#664efe',
        padding: 10,
        marginVertical: 5,
        marginHorizontal: 10,
    },
})

export default CardsList