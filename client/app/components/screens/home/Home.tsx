import { FC } from 'react'
import { StyleSheet, Text, View , SafeAreaView} from 'react-native'

const Home: FC = () => {
    return (
        <SafeAreaView style={styles.container}>
            <Text style={{fontSize: 20, color: '#5642d7'}}>
                Скоро здесь будет много всего!
            </Text>
        </SafeAreaView>
    )
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      alignItems: 'center',
      justifyContent: 'center',
    }
})

export default Home