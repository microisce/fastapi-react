export interface IBook {
    name: string,
    image: string,
    author: string,
}

export interface ILang{
    name: string,
    frameworks?: IFramework[]
}

export interface IFramework {
    name: string,
    language?:string,
    stack: string
}
