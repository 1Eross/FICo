import { ComponentType } from 'react'

export type TypeRootStackParamList = {
    Auth: undefined
    Home: undefined
    Settings: undefined
    Profile: undefined
    Statistics: undefined
}

export interface IRoute{
    name: keyof TypeRootStackParamList
    component: ComponentType
}