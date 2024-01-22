import { IUser } from '@/types/user.interface';
export interface IProfile extends Pick<IUser,'email'> {
    name: string
    words: string
    phone: string
}