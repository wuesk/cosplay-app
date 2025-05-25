export interface ILocation {
    name: string;
    lat: number;
    lng: number;
    description: string;
    friendly?: boolean;
    friendlyDescription?: string;
    legal?: boolean;
    legalDescription?: string;
    paid?: boolean;
    paidDescription?: string;
    parking?: boolean;
    parkingDescription?: string;
    link?: string;
    image?: string;
}