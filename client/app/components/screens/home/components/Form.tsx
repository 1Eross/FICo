import React from 'react'
import { View } from 'my-app/components/Themed'
import { StyleSheet, Text,  Button,TextInput, Image, TouchableNativeFeedback, SafeAreaView} from 'react-native'
import { Formik, FormikHelpers, FormikValues } from 'formik'

const Form = () => {
    return (
        <SafeAreaView>
            <Formik initialValues={{name: '', desc: '', category: ''}} onSubmit={(values) => {console.log(values)}}>
                {(props) => (
                    <View style={styles.View}>
                        <TextInput style={styles.text} value={props.values.name} placeholder='Введите сумму' onChangeText={props.handleChange('name')}>
                        </TextInput>
                        <TextInput style={styles.text} value={props.values.desc} multiline placeholder='Введите описание' onChangeText={props.handleChange('desc')}>
                        </TextInput>
                        <TextInput style={styles.text} value={props.values.category} placeholder='Введите категорию' onChangeText={props.handleChange('category')}>
                        </TextInput>
                        <TouchableNativeFeedback onPress={props.handleSubmit}>
                            <Image 
                                style={styles.buttonImage} 
                                source={require('../assets/okButton.png')}
                            />
                        </TouchableNativeFeedback>
                    </View>
                )}
            </Formik>
        </SafeAreaView>
    )
}

const styles = StyleSheet.create({
    buttonImage: {
        width: 60,
        height: 60,
    },
    View: {
        backgroundColor: '#1c1c2e',
        justifyContent: 'center',
        alignItems: 'center',
    },
    text: {
        fontSize: 20,
        color: '#664efe',
    }
})

export default Form