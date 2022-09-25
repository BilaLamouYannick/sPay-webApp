import React from 'react';
import {Image, StyleSheet, Text, View} from 'react-native';
import { ScrollView, TouchableOpacity } from 'react-native-gesture-handler';
import { useNavigation } from '@react-navigation/core';

const listService = [
  {
    name: 'Wallet',
    icon: require('../assets/ic_wallet.png'),
    navDirection: 'Wallet',
  },
  {
    name: 'Transfer',
    icon: require('../assets/ic_transfer.png'),
    navDirection: 'Transfer',
  },
  {
    name: 'Deposit',
    icon: require('../assets/ic_pay.png'),
    navDirection: 'Deposit',
  },
  {
    name: 'Withdraw',
    icon: require('../assets/ic_topup.png'),
    navDirection: 'Withdraw',
  },
  
];

const renderServiceItem = item => {
  const navigation = useNavigation();
  return (
    <View key={item.name} style={styles.items}>
      <TouchableOpacity onPress = {()=> navigation.navigate(item.navDirection,  {
        user: props.user, transactions: props.transactions, wallet: props.wallet
      })}>
      <View style={styles.icon}>
        <Image source={item.icon} />
      </View>
      
      <Text style={styles.itemText}>{item.name}</Text>
      </TouchableOpacity>
    </View>
  );
};

const ListService = (props) => {
  return (
    <ScrollView style={{bottom:0, position:'absolute', alignSelf:'center'}}>
      {/*<Text style={styles.title}>Service</Text>*/}
      <View style={styles.list}>{listService.map(renderServiceItem)}</View>
    </ScrollView>
  );
};

export default ListService;

const styles = StyleSheet.create({
  title: {
    fontWeight: 'bold',
    fontSize: 18,
  },
  list: {
    flexDirection: 'row',
    justifyContent: 'center',
    marginTop: 12,
    alignItems:'center'
  },
  icon: {
    padding: 10,
    backgroundColor: 'white',
    width: 60,
    height: 60,
    shadowColor: '#000',
    shadowOffset: {height: 10, width: 2},
    shadowOpacity: 0.7,
    shadowRadius: 80,
    borderRadius: 10,
    justifyContent: 'center',
    alignItems: 'center',
  
  },
  items: {
    justifyContent: 'center',
    alignItems: 'center',
    
  },
  itemText: {
    margin: 10,
    marginLeft:5
  },
});
