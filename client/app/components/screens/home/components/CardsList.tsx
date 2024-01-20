import React from 'react'
import { View } from 'my-app/components/Themed'
import { StyleSheet, Text, FlatList, } from 'react-native'

const CardsData = [
    {
        id: '1',
        name: '1000',
        desc: 'Таблеточки',
        category: 'Медицина',
    },
    {
        id: '2',
        name: '500',
        desc: '',
        category: 'Развлечения',
    },
    {
        id: '3',
        name: '350',
        desc: 'Проезд до универа',
        category: 'Транспорт',
    },
    {
        id: '4',
        name: '1500',
        desc: '',
        category: '',
    },
    {
        id: '5',
        name: '800',
        desc: '',
        category: '',
    },
    
]

const Item = ({item}: any,) => (
    <View style={styles.View}>
        <Text style={styles.text1}> {item.name} </Text>
        <Text style={styles.text2}> {item.desc} </Text>
        <Text style={styles.text3}> {item.category} </Text>

    </View>
)

const CardsList = () => {
    return (
            <FlatList 
            data={CardsData}
            renderItem={Item}
            keyExtractor={item => item.id}
            style={styles.List}>
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