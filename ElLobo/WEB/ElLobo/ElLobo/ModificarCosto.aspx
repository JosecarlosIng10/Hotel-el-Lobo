<%@ Page Title="" Language="C#" MasterPageFile="~/Opciones.master" AutoEventWireup="true" CodeBehind="ModificarCosto.aspx.cs" Inherits="ElLobo.ModificarCosto" %>
<asp:Content ID="Content1" ContentPlaceHolderID="contenidoPrincipal" runat="server">
    <p>
    <h2>CUENTA: 
        <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
    </h2>
    <p>
       <h2>CUENTA: 
        <asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
    </h2>
    <p><h2>COSTO: 
        <asp:TextBox ID="TextBox3" runat="server"></asp:TextBox>
    </h2>&nbsp;<p>
        <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="MODIFICAR" Width="106px" />
    </p>
</asp:Content>
