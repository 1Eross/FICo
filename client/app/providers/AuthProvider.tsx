import * as Splash from 'expo-splash-screen'
import { Dispatch, createContext, FC, SetStateAction, PropsWithChildren, useState, useEffect } from 'react'
import { Text, View } from 'react-native'
import type { IUser } from '@/types/user.interface'

export type TypeUserState = IUser | null

interface IContext{
    user: TypeUserState
    setUser: Dispatch<SetStateAction<TypeUserState>>
}

export const AuthContext = createContext({} as IContext)

let ignore = Splash.preventAutoHideAsync()

const AuthProvider: FC<PropsWithChildren<unknown>> = ({children}) => {
    const [user, setUser] = useState<TypeUserState>({} as IUser)

    useEffect(()=> {
        let isMounted = false

        const getUserFromStorage = async () => {

            if(isMounted){
                // Get user from async storage and write to store
            }
        
        await Splash.hideAsync()
        }

        let ignore = getUserFromStorage()

        

        return () => {
            isMounted = false
        }
    }, [])

    return (
        <AuthContext.Provider value={{ user, setUser }}>
            {children}
        </AuthContext.Provider>
    )
}

export default AuthProvider