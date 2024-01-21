import React from 'react'
import { View } from 'my-app/components/Themed'
import { StyleSheet, Text,  Button,TextInput, Image, TouchableOpacity, SafeAreaView} from 'react-native'
import { Formik, FormikHelpers, FormikValues } from 'formik'

const Form = ({addCard}) => {
    return (
        <SafeAreaView>
            <Formik initialValues={{number: '', category: '', data: ''}} onSubmit={(values, action) => {addCard(values), action.resetForm}}>
                {(props) => (
                    <View style={styles.ViewMain}>
                        <View style={styles.View}>
                            <TextInput style={styles.input} value={props.values.number} placeholder='Введите сумму' onChangeText={props.handleChange('number')}>
                            </TextInput>
                            <TextInput style={styles.input} value={props.values.category} placeholder='Введите категорию' onChangeText={props.handleChange('category')}>
                            </TextInput>
                            <TextInput style={styles.input} value={props.values.data} placeholder='Введите дату' onChangeText={props.handleChange('data')}>
                            </TextInput>
                        </View>
                            <TouchableOpacity onPress={props.handleSubmit}>
                                <Image 
                                    style={styles.buttonImage} 
                                    source={require('../assets/okButton.png')}
                                />
                            </TouchableOpacity>
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
    ViewMain: {
        backgroundColor: '#1c1c2e',
        justifyContent: 'center',
        alignItems: 'center',
        // width: '100%',
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
        backgroundColor: 'white',
    }
})

export default Form