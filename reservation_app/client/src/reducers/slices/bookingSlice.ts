import {createSlice, type PayloadAction} from '@reduxjs/toolkit'

interface Booking {
    id:string
    restaurantName:string
    date:string
    time:string
    numberOfGuests:number
}
interface BookingState{
    bookings:Booking[]
    loading:boolean
}
const initialState:BookingState={
    bookings:[],
    loading:false
}
const bookingSlice=createSlice({
    name:'booking',
    initialState,
    reducers:{
        setBookings:(state,action:PayloadAction<Booking[]>)=>{
            state.bookings=action.payload
        },
        addBooking:(state,action:PayloadAction<Booking>)=>{
            state.bookings.push(action.payload)
        },
        removeBooking:(state,action:PayloadAction<string>)=>{
            state.bookings=state.bookings.filter(booking=>booking.id!==action.payload)
        }
    }
})
export const{setBookings,addBooking,removeBooking}=bookingSlice.actions
export default bookingSlice.reducer