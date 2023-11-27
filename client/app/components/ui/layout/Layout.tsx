import { FC, PropsWithChildren } from 'react'
import { Platform, SafeAreaView, Text, View} from 'react-native'
import {  useSafeAreaInsets } from 'react-native-safe-area-context'

const Layout: FC<PropsWithChildren<{title?:string}>> = ({ children, title }) => {
    const { top } = useSafeAreaInsets()

    return (
    <SafeAreaView className='flex-1'>
        <View className='flex-1 px-6' style= {{
            paddingTop: Platform.OS === 'ios' ? top /5 : top * 1.6
        }}
        >
            {title &&<Text className='text-3xl text-center font-semibond text-white'>{title}</Text>}
        
        <View className='flex-1'>
        {children}
        </View>
        </View>
    </SafeAreaView>
    )
}
export default Layout