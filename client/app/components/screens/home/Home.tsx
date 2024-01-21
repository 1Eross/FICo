import { View } from 'my-app/components/Themed'
import { FC, useState } from 'react'
import { StyleSheet, Text, SafeAreaView, Alert, Image, TouchableNativeFeedback, Modal} from 'react-native'
import CardsList from './components/CardsList'
import Form from './components/Form'
import { list } from 'postcss'

const Home: FC = () => {
    const buttonPress = () => {
        Alert.alert("Добавить трату", "", [
            {text: "Ок", onPress: () => console.log('Ok')},
            {text: 'Отмена', onPress: () => console.log('Отмена')}
        ])
    }

    const [modalWindow, setModalWindow] = useState(false);

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
                        <Form />
                    </View>
                    <View style={styles.ModalButtons}>
                        <TouchableNativeFeedback onPress={() => setModalWindow(false)}>
                            <Image 
                                style={styles.buttonImage} 
                                source={require('./assets/cancelButton.png')}
                            />
                        </TouchableNativeFeedback> 
                    </View>
                </SafeAreaView>
            </Modal>
            

            <View style={styles.viewCircle}>
                <Text style={styles.text}>
                    Здесь будет кружок трат?
                </Text>
            </View>

            <View style={styles.viewCards}>
                <CardsList />
            </View>

            <View style={styles.viewButton}>
                <TouchableNativeFeedback onPress={() => setModalWindow(true)}>
                    <Image 
                        style={styles.buttonImage} 
                        source={require('./assets/addButton.png')}
                    />
                </TouchableNativeFeedback>
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
    
    
    buttonImage: {
        width: 60,
        height: 60,
    },
    text: {
        fontSize: 25,
        color: '#664efe',
    }
})

export default Home