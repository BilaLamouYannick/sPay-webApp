import React from 'react';
import {Image, StyleSheet, Text, View, TouchableOpacity} from 'react-native';
import { ScrollView } from 'react-native-gesture-handler';
import { AddModal } from './AddModal';

const listTransations = [
  {
    type: 'Spotify',
    icon: require('../assets/ic_spotify.png'),
    date: 'Jun 12, 12:30',
    payment: '+ $12',
  },
  {
    type: 'Paypal',
    icon: require('../assets/ic_paypal.png'),
    date: 'Jun 12, 12:30',
    payment: '+ $12',
  },
  {
    type: 'Dribble',
    icon: require('../assets/ic_dribble.png'),
    date: 'Jun 12, 12:30',
    payment: '+ $14',
  },
  {
    type: 'Other1',
    icon: require('../assets/ic_dribble.png'),
    date: 'Jun 12, 12:30',
    payment: '+ $14',
  },
  {
    type: 'Other2',
    icon: require('../assets/ic_dribble.png'),
    date: 'Jun 12, 12:30',
    payment: '+ $14',
  },
  {
    type: 'Other3',
    icon: require('../assets/ic_dribble.png'),
    date: 'Jun 12, 12:30',
    payment: '+ $14',
  },
];


export const LastTransactions = (props) =>{
  const [modalVisible, setModalVisible] = React.useState(false)
  const transactions = props.transactions
  const user = props.user
  const tester = (userEmail,transactionReceiver) =>{return (userEmail==transactionReceiver)? true:false}
  return( 
  <View style={styles.container}>
    {transactions.map((item )=>(
      <TouchableOpacity onPress={() => setModalVisible(false)}>
      <View key={item.uid} style={styles.items}>
      
        <Image source={require('../assets/logo_mtn_1.png')} style={{resizeMode:'contain', height: 35, width:35, borderRadius:50}}/>
      
      <View style={styles.itemBody}>
        <Text style={styles.operator}>{item.operator}</Text>
        <Text style={styles.receiver}>{tester(user.email, item.receiver)? 'Deposit received':  ` Transfer to  ${item.receiver}`}</Text>
        <Text style={styles.receiver}>{item.status}</Text>
      </View>
      <View>
        <Text style={styles.amount}>{item.amount} FCFA</Text>
      </View>
    </View>
    </TouchableOpacity>
    )
    )}
    <AddModal visible={modalVisible}>
      <View>
        <TouchableOpacity onPress={()=>setModalVisible(false)}>
          <Text style={{}}> close </Text>
          </TouchableOpacity>
      </View>

    </AddModal>
    
    {console.log(modalVisible)}
  </View>
    
  );};

const renderTransactionItem = item => (
    
  <View key={item.type} style={styles.items}>
    <View style={styles.icon}>
      <Image source={item.icon} />
    </View>
    <View style={styles.itemBody}>
      <Text style={styles.type}>{item.type}</Text>
      <Text style={styles.date}>{item.date}</Text>
    </View>
    <View>
      <Text style={styles.payment}>{item.payment}</Text>
    </View>
  </View>
  
);

const RecentTransaction = () => {
  return (
    <View style={styles.container}>
      {/* <Text style={styles.title}>Recent Transaction</Text> */}
      {/* <ScrollView style={styles.list}>
        {listTransations.map(renderTransactionItem)}
      </ScrollView> */}
      {listTransations.map(renderTransactionItem)}
    </View>
  );
};

//export default RecentTransaction;
export default renderTransactionItem;

const styles = StyleSheet.create({
  title: {
    fontWeight: 'bold',
    fontSize: 18,
  },
  list:{
    
  },
  container: {
    marginTop: 10,
  },
  items: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 2,
    borderBottomWidth:.5,
    borderBottomColor: "#9C9D9E"
  },
  icon: {
    padding: 5,
    backgroundColor: 'white',
    width: 30,
    height: 30,
    shadowColor: '#000',
    shadowOffset: {height: 10, width: 2},
    shadowOpacity: 0.7,
    shadowRadius: 80,
    borderRadius: 10,
    justifyContent: 'center',
    alignItems: 'center',
  },
  itemBody: {
    flex: 1,
    paddingLeft: 5,
   
  },
  // type: {
  //   fontWeight: 'bold',
  //   fontSize: 16,
  //   color:'#FFF',
  // },
  operator: {
    fontWeight: 'bold',
    fontSize: 16,
    color:'#FFF',
  },
  // date: {
  //   marginTop: 3,
  //   color:'#FFF',
  //   fontSize: 10
  // },
  receiver: {
    marginTop: 3,
    color:'#FFF',
    fontSize: 10
  },

  // payment: {
  //   fontWeight: 'bold',
  //   fontSize: 16,
  //   color:'#FFF'
  // },
  amount: {
    fontWeight: 'bold',
    fontSize: 13,
    color:'#FFF'
  },
});
