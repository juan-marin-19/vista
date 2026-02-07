import { StatusBar } from "expo-status-bar";
import { useEffect, useState } from "react";
import { SafeAreaView, StyleSheet, Text, View } from "react-native";
import axios from "axios";

const API_BASE = process.env.EXPO_PUBLIC_API_BASE || "http://localhost:8000/api";

export default function App() {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    const fetchAlerts = async () => {
      try {
        const response = await axios.get(`${API_BASE}/alerts/`);
        setAlerts(response.data);
      } catch (error) {
        setAlerts([]);
      }
    };
    fetchAlerts();
  }, []);

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>VRISA móvil</Text>
        <Text style={styles.subtitle}>Alertas en tiempo real</Text>
      </View>
      <View style={styles.card}>
        {alerts.length === 0 ? (
          <Text style={styles.empty}>No hay alertas disponibles.</Text>
        ) : (
          alerts.map((alert) => (
            <View key={alert.id} style={styles.alertItem}>
              <Text style={styles.alertTitle}>{alert.title}</Text>
              <Text style={styles.alertSeverity}>{alert.severity}</Text>
            </View>
          ))
        )}
      </View>
      <StatusBar style="auto" />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#f8fafc",
    padding: 24
  },
  header: {
    marginTop: 24,
    marginBottom: 16
  },
  title: {
    fontSize: 28,
    fontWeight: "700",
    color: "#0f172a"
  },
  subtitle: {
    fontSize: 16,
    color: "#475569"
  },
  card: {
    backgroundColor: "#fff",
    borderRadius: 16,
    padding: 16,
    shadowColor: "#0f172a",
    shadowOpacity: 0.1,
    shadowRadius: 12
  },
  empty: {
    color: "#94a3b8"
  },
  alertItem: {
    paddingVertical: 8
  },
  alertTitle: {
    fontSize: 16,
    fontWeight: "600"
  },
  alertSeverity: {
    color: "#ef4444"
  }
});
