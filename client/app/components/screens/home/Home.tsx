import { View } from 'my-app/components/Themed'
import { FC, useState } from 'react'
import { StyleSheet, Text, SafeAreaView, FlatList, Image, TouchableOpacity, Modal} from 'react-native'
// import CardsList from './components/CardsList'
import Form from './components/Form'
import { list } from 'postcss'

const Home: FC = () => {

    const [modalWindow, setModalWindow] = useState(false);

    const [cardsData, setCards] = useState([]);

    const addCard = (card: any) => {
        setCards((list) => {
            card.id = Math.random().toString()
            return [
                card,
                ...list
            ]
        })
        setModalWindow(false)
    }

    const dellCard = (cardId: any) => {
        setCards((prevData) => prevData.filter((item) => item.id !== cardId))
    }

    const handleRemoveCard = (cardId: any) => {
        dellCard(cardId);
      };


    return (
        <SafeAreaView style={styles.safeAreaView}>
            <Modal visible={modalWindow}>
                <SafeAreaView style={styles.ModalMain}>
                    <View style={styles.ModalText}>
                        <Text style={styles.text}>
                            Добавление траты
                        </Text>
                    </View>
                    <View style={styles.ModalText}>
                        <Form addCard={addCard}/>
                    </View>
                    <View style={styles.ModalButtons}>
                        <TouchableOpacity onPress={() => setModalWindow(false)}>
                            <Image 
                                style={styles.buttonImage} 
                                source={require('./assets/cancelButton.png')}
                            />
                        </TouchableOpacity> 
                    </View>
                </SafeAreaView>
            </Modal>
            

            <View style={styles.viewCircle}>
                <Text style={styles.text}>
                    Здесь будет кружок трат?
                </Text>
            </View>

            <View style={styles.viewCards}>
                <FlatList 
                data={cardsData}
                renderItem={({item}) => (
                    <View style={styles.View}>
                        <View style={styles.ViewSmall}>
                            <Text style={styles.text1}>{item.number}</Text>
                            <Text style={styles.text2}>{item.category}</Text>
                            <Text style={styles.text3}>{item.data}</Text>
                        </View>
                        <View style={styles.ViewSmall2}>
                            <TouchableOpacity onPress={() => handleRemoveCard(item.id)}>
                                <Image 
                                    style={styles.buttonImage2} 
                                    source={require('./assets/dellButton.png')}
                                />
                            </TouchableOpacity>
                        </View>
                    </View>
                )}
                // dellCard={dellCard}
                style={styles.List}>
                </FlatList>
            </View>

            <View style={styles.viewButton}>
                <TouchableOpacity onPress={() => setModalWindow(true)}>
                    <Image 
                        style={styles.buttonImage} 
                        source={require('./assets/addButton.png')}
                    />
                </TouchableOpacity>
            </View>
            
        </SafeAreaView>
    )
}

const styles = StyleSheet.create({
    safeAreaView: {
      flex: 1,
    },
    viewCircle: {
        flex: 3.5,
        backgroundColor: '#1c1c2e',
        justifyContent: 'center',
        alignItems: 'center',
    },
    viewCards: {
        flex: 3.8,
        backgroundColor: '#1c1c2e',
        justifyContent: 'center',
        alignItems: 'center',
    },
    viewButton: {
        flex: 0.9,
        backgroundColor: '#1c1c2e',
        justifyContent: 'center',
        alignItems: 'center',
    },
    
    
    ModalMain: {
        flex: 1,
        backgroundColor: '#1c1c2e',
        justifyContent: 'center',
        alignItems: 'center',
    },
    ModalButtons: {
        backgroundColor: '#1c1c2e',
        justifyContent: 'center',
        alignItems: 'center',
        // flexDirection: 'row',
        // marginTop: 30,
    },
    ModalText: {
        backgroundColor: '#1c1c2e',
        justifyContent: 'center',
        alignItems: 'center',
        marginTop: 30,
    },


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
        flexDirection: 'row',
    },
    ViewSmall: {
        backgroundColor: '#664efe',
        flex: 8,
    },
    ViewSmall2: {
        backgroundColor: '#664efe',
        justifyContent: 'center',
        alignItems: 'flex-end',
        flex: 1,
    },
    
    
    buttonImage: {
        width: 60,
        height: 60,
    },
    buttonImage2: {
        width: 40,
        height: 40,

    },
    text: {
        fontSize: 25,
        color: '#664efe',
    }
})

export default Home