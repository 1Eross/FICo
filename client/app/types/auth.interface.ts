import { IUser } from  '@/types/user.interface'

export interface IAuthFormData extends Pick<IUser, 'email' | 'password'> {

}