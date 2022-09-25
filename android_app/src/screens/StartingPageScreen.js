
import React, { useState } from 'react';
import { SafeAreaView, Text, View, StyleSheet, Button } from 'react-native';
import Spinner from 'react-native-loading-spinner-overlay';
import { useNavigation } from '@react-navigation/core';

const Starter = () => {
  const [loading, setLoading] = useState(true);
  const navigation = useNavigation();
  const stopLoading = () => {
    setTimeout(() => {
      loading(false);
    }, 3000);
    
    
    navigation.navigate('Welcome')
  };

  return (
    <SafeAreaView style={{ flex: 1 }}>
      <View style={styles.container}>
        <Spinner
          visible={loading}
          textContent={'Loading...'}
          textStyle={styles.spinnerTextStyle}
        />
        <Text style={{ textAlign: 'center', fontSize: 40 }}>SPay</Text>
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    textAlign: 'center',
    paddingTop: 30,
    backgroundColor: '#ecf0f1',
    padding: 8,
  },
  spinnerTextStyle: {
    color: '#FFF',
  },
});

export default Starter;
