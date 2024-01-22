// user.interface.ts
export interface IUser {
    _id: string
    login: string
    password: string
    firstName?: string;
    lastName?: string;
  }