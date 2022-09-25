import React from "react";
import { View, StyleSheet,Text } from "react-native";
import {useNavigation} from '@react-navigation/core';



const Notificate = (props)=>{

return(
    <View style = {styles.container}>
        <Text style = {styles.title}>{props.title} </Text>
        <Text style = {styles.content}>{props.content} </Text>
        <Text style = {styles.date}>{props.date} </Text>
    </View>

);
};

export default Notificate;

const styles = StyleSheet.create({
    container: {
        backgroundColor: '#FFF',
        bordeBottomStyle: 'solide',
        borderColor: 'black',
        borderWeight: 2,
        marginBottom: 2,
    },
    title: {
        fontSize: 15,
        textAlign: 'center',
        fontweight: 'bold',
      },
      content: {
        fontSize: 15,
        textAlign: 'justify',
      },
      date: {
       fontSize: 10,
       textAlign: 'right',
      },
  });