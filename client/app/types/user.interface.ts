export interface IUser {
  _id: string
  login: string
  password: string
  email?: string;
  phoneNumber?: string;
  firstName?: string;
  lastName?: string;
}