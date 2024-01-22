import React from 'react'
import { View, } from 'my-app/components/Themed'
import { StyleSheet, TextInput, Image, TouchableOpacity, SafeAreaView,} from 'react-native'
import { Formik } from 'formik'
import {Picker} from '@react-native-picker/picker'
import MaskedInput from 'react-text-mask'


const Form = ({addCard}) => {
    
    return (
        <SafeAreaView>
            <Formik initialValues={{number: '', category: '', data: ''}} onSubmit={(values, action) => {addCard(values), action.resetForm}}>
                {(props) => (
                    <View style={styles.ViewMain}>
                        <View style={styles.View}>
                            <TextInput
                                style={styles.input}
                                value={props.values.number}
                                keyboardType={'numeric'}
                                placeholder='Введите сумму'
                                placeholderTextColor='#664efe'
                                onChangeText={props.handleChange('number')}>
                            </TextInput> 
                            <Picker style={styles.picker} selectedValue={props.values.category} onValueChange={props.handleChange('category')}>
                                <Picker.Item label="" value="" />
                                <Picker.Item label="Учёба" value="Учёба" />
                                <Picker.Item label="Семья" value="Семья" />
                                <Picker.Item label="Здоровье" value="Здоровье" />
                                <Picker.Item label="Продукты" value="Продукты" />
                                <Picker.Item label="Кафе" value="Кафе" />
                                <Picker.Item label="Досуг" value="Досуг" />
                                <Picker.Item label="Транспорт" value="Транспорт" />
                                <Picker.Item label="Подарки" value="Подарки" />
                                <Picker.Item label="Покупки" value="Покупки" />
                            </Picker>
                            {/* <MaskedInput
                                style={styles.input}
                                mask={[/\d/, /\d/, /\d/, /\d/, '-', /\d/, /\d/, '-', /\d/, /\d/]}
                                placeholder='YYYY-MM-DD'
                                value={props.values.data}
                                onChange={props.handleChange('data')}>
                            </MaskedInput> */}
                            <TextInput
                                style={styles.input}
                                value={props.values.data}
                                keyboardType={'numeric'}
                                placeholder='YYYY-MM-DD'
                                placeholderTextColor='#664efe'
                                onChangeText={props.handleChange('data')}>
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