import { IUser } from '@/types/user.interface';
export interface IAuthFormData extends Pick<IUser, 'login' | 'password' | 'email' | 'phoneNumber'> {
  firstName?: string;
  lastName?: string;
}