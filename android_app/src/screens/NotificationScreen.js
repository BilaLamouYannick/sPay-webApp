import React from "react";
import { ScrollView, StyleSheet } from "react-native";
import {useNavigation} from '@react-navigation/core';
import Notificate from "../components/NotificationComponent";

const listNotification = [
    { 
      title: 'Title 1',
      content: 'you receive 19$',
      date: '30-09-2000',
    },
    {
        title: 'Title 2',
        content: 'you receive 5$',
        date: '23-10-2001',
    },
    {
        title: 'Title 3',
        content: 'take care of your 19$',
        date: '02-11-2020',
    },
    {
        title: 'Title 4',
        content: 'you receive 19$',
        date: '23-03-2000',
    },
    {
        title: 'Title 5',
        content: 'you receive 19$',
        date: '30-09-2000',
    },
    {
        title: 'Title 6',
        content: 'you receive 19$',
        date: '30-09-2000',
    },
    {
        title: 'Title 7',
        content: 'you receive 19$',
        date: '30-09-2000',
    },
    {
        title: 'Title 8',
        content: 'you seded 19$',
        date: '30-09-2000',
    },
    {
        title: 'Title 9',
        content: 'you receive 19$',
        date: '30-09-2000',
    },
    {
        title: 'Title 10',
        content: 'you receive 19$',
        date: '30-09-2000',
    },
    {
        title: 'Title 11',
        content: 'you receive 19$',
        date: '30-09-2000',
    },
    {
        title: 'Title 12',
        content: 'you receive 19$',
        date: '30-09-2000',
    },
    
  ];
  

const Notification = ()=>{
    const navigation = useNavigation();
    const notif = listNotification.map((item) => <Notificate title ={item.title} content = {item.content} date = {item.date} />);

return(
    <ScrollView style = {styles.container} >
        {notif}

    </ScrollView>

);
};

export default Notification;

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#1a1918',
      margin: 15,
      marginTop:50
    },
  });
  