import { View } from 'my-app/components/Themed'
import { FC } from 'react'
import { StyleSheet, Text, SafeAreaView, Button, Alert, Image, TouchableNativeFeedback} from 'react-native'

const Home: FC = () => {
    const buttonPress = () => {
        Alert.alert("Добавить трату", "", [
            {text: "Ок", onPress: () => console.log('Ok')},
            {text: 'Отмена', onPress: () => console.log('Отмена')}
        ])
    }

    return (
        <SafeAreaView style={styles.safeAreaView}>
            <View style={styles.viewCircle}>
                <Text style={styles.text}>
                    Здесь будет кружок трат!
                </Text>
            </View>

            <View style={styles.viewCards}>
                <Text style={styles.text}>
                    Здесь будет список трат!
                </Text>
            </View>

            <View style={styles.viewButton}>
                <TouchableNativeFeedback onPress={buttonPress}>  
                    <Image style={styles.buttonImage} source={{
                        uri: 'https://www.pngall.com/wp-content/uploads/10/Plus-Symbol-Vector-No-Background.png',
                    }}/>
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
        flex: 1,
        backgroundColor: '#1c1c2e',
        justifyContent: 'center',
        alignItems: 'center',
    },
    buttonImage: {
        width: 65,
        height: 65,
        left: 0,
    },
    text: {
        fontSize: 20,
        color: '#664efe',
    }
})

export default Home